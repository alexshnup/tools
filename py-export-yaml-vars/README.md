# YAML Environment Variable Exporter

## Overview
This script parses a given YAML file and exports its variables as environment variables with a specific prefix.

## Usage
To use the script, run it with the path to your YAML file as an argument:

```bash
python your_script.py path_to_your_yaml_file.yml
```

This will print export commands for each variable found in the YAML file. To export these variables to your current terminal session, use:

```bash
source <(python your_script.py path_to_your_yaml_file.yml)
```

## Requirements
-Python 3
-PyYAML package

Install PyYAML using pip:
```
pip install pyyaml
```

## Example

