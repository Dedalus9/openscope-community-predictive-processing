import os
import yaml
import glob
import importlib.util
from collections import defaultdict

# Path to the mkdocs.yml file
MKDOCS_YML_PATH = "mkdocs.yml"

# Directories to scan for markdown files
EXPERIMENTS_DIR = "docs/experiments"
MEETINGS_DIR = "docs/meetings"

# Path to sync script
SYNC_SCRIPT_PATH = "code/utils/sync_experiment_summary.py"

def get_markdown_files(directory):
    """Get a sorted list of markdown files in a directory."""
    if not os.path.exists(directory):
        return []
    return sorted(
        [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".md")]
    )

def get_hierarchical_markdown_files(directory):
    """
    Get a hierarchical structure of markdown files from a directory and its subdirectories.
    Returns a dictionary with lab as key and another dictionary as value with platform as key and list of files as value.
    """
    if not os.path.exists(directory):
        return {}
    
    hierarchy = defaultdict(lambda: defaultdict(list))
    
    # Use glob to find all .md files in the directory and its subdirectories
    for filepath in sorted(glob.glob(f"{directory}/**/*.md", recursive=True)):
        rel_path = os.path.relpath(filepath, "docs")
        
        # Skip files directly in the experiments directory (old format)
        if os.path.dirname(rel_path) == "experiments":
            continue
            
        # Extract lab and platform from the path
        parts = rel_path.split(os.sep)
        if len(parts) >= 3:  # experiments/lab_name/platform/file.md
            lab = parts[1]
            platform = parts[2]
            hierarchy[lab][platform].append(filepath)
    
    return hierarchy

def format_nav_entry(filepath):
    """Format the nav entry to include the filename as the display name."""
    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]  # Remove the .md extension
    return {name: os.path.relpath(filepath, "docs")}

def sync_experiment_summary():
    """Synchronize the experiment summary page with individual experiment files."""
    print("Syncing experiment summary with individual experiment files...")
    
    # Import and execute the sync_experiment_summary script
    spec = importlib.util.spec_from_file_location("sync_module", SYNC_SCRIPT_PATH)
    sync_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sync_module)
    
    # Call the main function from the imported script
    sync_module.main()

def update_mkdocs():
    """Update the mkdocs.yml file to include all markdown files dynamically."""
    # Load the existing mkdocs.yml
    with open(MKDOCS_YML_PATH, "r") as f:
        mkdocs_config = yaml.safe_load(f)

    # Ensure 'nav' exists and is a list
    if "nav" not in mkdocs_config or not isinstance(mkdocs_config["nav"], list):
        mkdocs_config["nav"] = []

    # Find the Project Resources and Project Management sections
    project_resources_index = None
    project_management_index = None
    
    for i, item in enumerate(mkdocs_config["nav"]):
        if isinstance(item, dict) and "Project Resources" in item:
            project_resources_index = i
        if isinstance(item, dict) and "Project Management" in item:
            project_management_index = i
    
    # Remove existing Experiments section from Project Resources
    if project_resources_index is not None:
        project_resources = mkdocs_config["nav"][project_resources_index]["Project Resources"]
        project_resources = [item for item in project_resources if not (isinstance(item, dict) and "Experiments" in item)]
        mkdocs_config["nav"][project_resources_index]["Project Resources"] = project_resources
    
    # Remove existing Meetings section from Project Management
    if project_management_index is not None:
        project_management = mkdocs_config["nav"][project_management_index]["Project Management"]
        project_management = [item for item in project_management if not (isinstance(item, dict) and "Meetings" in item)]
        mkdocs_config["nav"][project_management_index]["Project Management"] = project_management
    
    # Add updated hierarchical Experiments section to Project Resources
    experiments_hierarchy = get_hierarchical_markdown_files(EXPERIMENTS_DIR)
    if experiments_hierarchy:
        experiments_nav = []
        
        for lab, platforms in experiments_hierarchy.items():
            lab_nav = []
            
            for platform, files in platforms.items():
                platform_entries = [format_nav_entry(f) for f in files]
                lab_nav.append({platform: platform_entries})
            
            experiments_nav.append({lab: lab_nav})
        
        if project_resources_index is not None:
            mkdocs_config["nav"][project_resources_index]["Project Resources"].append(
                {"Experiments": experiments_nav}
            )
    
    # Add updated Meetings section to Project Management
    meetings_files = get_markdown_files(MEETINGS_DIR)
    if meetings_files:
        meetings_entries = [format_nav_entry(f) for f in meetings_files]
        if project_management_index is not None:
            mkdocs_config["nav"][project_management_index]["Project Management"].append(
                {"Meetings": meetings_entries}
            )
    
    # Save the updated mkdocs.yml
    with open(MKDOCS_YML_PATH, "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)
    
    # Sync experiment summary with individual experiment files
    sync_experiment_summary()

if __name__ == "__main__":
    update_mkdocs()