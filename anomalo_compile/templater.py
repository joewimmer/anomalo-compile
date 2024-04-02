import os
import jinja2
import yaml
from deepmerge import Merger

from anomalo_compile.filters import custom_filter


def compile_templates_to_yaml(base_directory: str = "./", vars_files: list = [], template_files: list = []):
    # Set up the Jinja2 environment
    directory_path = f"{base_directory}/templates"
    rendered_path = f"{base_directory}/rendered"
    vars_path = f"{base_directory}/vars"

    template_loader = jinja2.FileSystemLoader(searchpath=directory_path)
    template_env = jinja2.Environment(loader=template_loader)
    
    # Add the custom filter to the Jinja2 environment
    # template_env.filters["custom_filter"] = custom_filter

    
    # Iterate through all files in the directory
    for filename in template_files:
        if filename.endswith(".j2"):
            template_path = os.path.join(directory_path, filename)
            try:
                # Load the template by name
                template = template_env.get_template(filename)
                # Compile the context data
                context_data = compile_vars(vars_path=vars_path, vars_files=vars_files)
                # Render the template with the YAML context data
                rendered_yaml = template.render(context_data)

                # Ensure rendered_path directory exists
                if not os.path.exists(rendered_path):
                    os.makedirs(rendered_path)

                # Define the output filename and path
                output_filename = filename[:-3] + ".yaml"  # Change the extension
                output_path = os.path.join(rendered_path, output_filename)

                # Write the rendered YAML to a file
                with open(output_path, "w") as output_file:
                    output_file.write(rendered_yaml)
                print(f"Successfully compiled {template_path} to {output_path}")

            except Exception as e:
                print(f"Error processing {template_path}: {e}")


def compile_vars(vars_path="./vars", vars_files=[]):
    my_merger = Merger(
        [
            (list, ["append"]),  # or use "union" for deduplication
            (dict, ["merge"]),
        ],
        # next, choose the fallback strategies,
        # applied to all other types:
        ["override"],
        # finally, choose the strategies in
        # case of conflict:
        ["override"]
    )
    
    # Initialize the context data dictionary
    yaml_data = {}
    
    merged_dict = {}
    # Loop through all YAML files in the vars directory
    
    # Sort the files to ensure consistent ordering
    # vars_files.sort()
    # For each file, load the YAML data into the context dictionary
    for yaml_file in vars_files:
        with open(f"{vars_path}/{yaml_file}", "r") as file:
            # Load the YAML data into the context dictionary
            yaml_data = yaml.safe_load(file)
            merged_dict = my_merger.merge(merged_dict, yaml_data)
            
    # Return the compiled context data
    return merged_dict

