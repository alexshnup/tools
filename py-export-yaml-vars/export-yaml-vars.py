
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
