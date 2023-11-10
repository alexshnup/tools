
# apk add python3
# pip3 install pyyaml

# cat values.yaml

# global:
#   domain:
#     - example1.com
#     - example2.com
#   EmailSenderSetup:
#     Password: "default"
#     EnableSsl: False
#   RefreshTokenLifetime: 3600
#   rabbitmq:
#     pass: "default"
#   requests:
#     rabbitmq:
#       cpu: 400m
#       memory: 1024Mi

#    - source <(python3 deploy/export-yaml-vars.py deploy/helm/values.yaml)
#    - env | grep YAML_ENV

# YAML_ENV_GLOBAL_GLOBAL_DOMAIN=[example1.com, example2.com]
# YAML_ENV_GLOBAL_GLOBAL_EMAILSENDERSETUP_PASSWORD=default
# YAML_ENV_GLOBAL_GLOBAL_EMAILSENDERSETUP_ENABLESSL=False
# YAML_ENV_GLOBAL_GLOBAL_REFRESHTOKENLIFETIME=3600
# YAML_ENV_GLOBAL_GLOBAL_RABBITMQ_PASS=default
# YAML_ENV_GLOBAL_GLOBAL_REQUESTS_RABBITMQ_CPU=400m
# YAML_ENV_GLOBAL_GLOBAL_REQUESTS_RABBITMQ_MEMORY=1024Mi

import yaml
import os
import argparse

def parse_and_export(yaml_content, prefix='', path=''):
    if isinstance(yaml_content, dict):
        for key, value in yaml_content.items():
            new_path = f"{path}.{key}" if path else key
            parse_and_export(value, prefix, new_path)
    else:
        env_var = f"{prefix}_{path}".replace('.', '_').upper()
        print(f"export {env_var}='{yaml_content}'")

def main(file_path):
    # Load YAML file
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    parse_and_export(yaml_data, 'YAML_ENV', 'global')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export YAML variables as environment variables.")
    parser.add_argument('file_path', help="Path to the YAML file")
    args = parser.parse_args()
    main(args.file_path)




