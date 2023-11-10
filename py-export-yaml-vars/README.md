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
```bash
pip install pyyaml
```

## Example

```bash
cat values.yaml

 global:
   domain:
     - example1.com
     - example2.com
   EmailSenderSetup:
     Password: "default"
     EnableSsl: False
   RefreshTokenLifetime: 3600
   rabbitmq:
     pass: "default"
   requests:
     rabbitmq:
       cpu: 400m
       memory: 1024Mi
```

```bash
source <(python3 deploy/export-yaml-vars.py deploy/helm/values.yaml)
env | grep YAML_ENV

 YAML_ENV_GLOBAL_GLOBAL_DOMAIN=[example1.com, example2.com]
 YAML_ENV_GLOBAL_GLOBAL_EMAILSENDERSETUP_PASSWORD=default
 YAML_ENV_GLOBAL_GLOBAL_EMAILSENDERSETUP_ENABLESSL=False
 YAML_ENV_GLOBAL_GLOBAL_REFRESHTOKENLIFETIME=3600
 YAML_ENV_GLOBAL_GLOBAL_RABBITMQ_PASS=default
 YAML_ENV_GLOBAL_GLOBAL_REQUESTS_RABBITMQ_CPU=400m
 YAML_ENV_GLOBAL_GLOBAL_REQUESTS_RABBITMQ_MEMORY=1024Mi
```
