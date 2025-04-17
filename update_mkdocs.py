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

def update_mkdocs():
    """Update the mkdocs.yml file to include all markdown files dynamically."""
    # Load the existing mkdocs.yml
    with open(MKDOCS_YML_PATH, "r") as f:
        mkdocs_config = yaml.safe_load(f)

    # Ensure 'nav' exists and is a list
    if "nav" not in mkdocs_config or not isinstance(mkdocs_config["nav"], list):
        mkdocs_config["nav"] = []

    # Remove existing Experiments and Meetings sections
    mkdocs_config["nav"] = [
        item for item in mkdocs_config["nav"] if not ("Experiments" in item or "Meetings" in item)
    ]

    # Add Experiments section
    experiments_files = get_markdown_files(EXPERIMENTS_DIR)
    if experiments_files:
        mkdocs_config["nav"].append(
            {"Experiments": [os.path.relpath(f) for f in experiments_files]}
        )

    # Add Meetings section
    meetings_files = get_markdown_files(MEETINGS_DIR)
    if meetings_files:
        mkdocs_config["nav"].append(
            {"Meetings": [os.path.relpath(f) for f in meetings_files]}
        )

    # Save the updated mkdocs.yml
    with open(MKDOCS_YML_PATH, "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    update_mkdocs()