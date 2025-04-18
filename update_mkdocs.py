import os
import yaml

# Path to the mkdocs.yml file
MKDOCS_YML_PATH = "mkdocs.yml"

# Directories to scan for markdown files
EXPERIMENTS_DIR = "docs/experiments"
MEETINGS_DIR = "docs/meetings"

def get_markdown_files(directory):
    """Get a sorted list of markdown files in a directory."""
    if not os.path.exists(directory):
        return []
    return sorted(
        [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".md")]
    )

def format_nav_entry(filepath):
    """Format the nav entry to include the filename as the display name."""
    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]  # Remove the .md extension
    return {name: os.path.relpath(filepath, "docs")}

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
    
    # Add updated Experiments section to Project Resources
    experiments_files = get_markdown_files(EXPERIMENTS_DIR)
    if experiments_files:
        experiments_entries = [format_nav_entry(f) for f in experiments_files]
        # Add the template link to experiments section
        experiments_entries.append({"Template": "templates/mouse_experiment_template.md"})
        
        if project_resources_index is not None:
            mkdocs_config["nav"][project_resources_index]["Project Resources"].append(
                {"Experiments": experiments_entries}
            )
    
    # Add updated Meetings section to Project Management
    meetings_files = get_markdown_files(MEETINGS_DIR)
    if meetings_files:
        meetings_entries = [format_nav_entry(f) for f in meetings_files]
        # Add the template link to meetings section
        meetings_entries.append({"Template": "templates/meeting_template.md"})
        
        if project_management_index is not None:
            mkdocs_config["nav"][project_management_index]["Project Management"].append(
                {"Meetings": meetings_entries}
            )
    
    # Save the updated mkdocs.yml
    with open(MKDOCS_YML_PATH, "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    update_mkdocs()