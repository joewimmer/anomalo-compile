import argparse
import os

import yaml
from .templater import compile_templates_to_yaml 

def main():
    parser = argparse.ArgumentParser(description='Compile Jinja2 templates into YAML configurations for Anomalo')
    parser.add_argument('environment', type=str, help='The environment to use for the compilation')
    parser.add_argument('directory', type=str, help='The directory containing the templates/ and vars/ directories')
    
    args = parser.parse_args()

    # Validate that the directory exists
    if not os.path.isdir(f"{args.directory}/templates"):
        print(f"The templates directory does not exist")
        return
    if not os.path.isdir(f"{args.directory}/vars"):
        print(f"The vars directory does not exist")
        return
    # Check the config.yaml file to see if there is an environment
    # If there is no environment, use the default
    environment_config = load_yaml(f"{args.directory}/config.yaml")
    
    environment = environment_config.get(args.environment, 'default')
    if not environment:
        print(f"No environment specified in the config.yaml file")
        return
    
    
    # Assuming you have a function to compile templates within the directory
    compile_templates_to_yaml(base_directory=args.directory, vars_files=environment['vars'], template_files=environment['templates'])
    
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    main()
