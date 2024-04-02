# Anomalo-Compile Project

## Overview
Anomalo-Compile is designed to allow users to render jinja2 templates for the Anomalo CLI. This is useful for users with multiple environments or need to make a bulk change.

## Getting Started
### Prerequisites
- Python 3.6+
- Pip

### Installation
Clone the repository and install the required Python packages:
```bash
git clone https://github.com/joewimmer/anomalo-compile.git
cd anomalo-compile
pip install -r requirements.txt

pip install -e .
```

### Usage
```bash
anomalo-compile --help

anomalo-compile lab .

anomalo-compile prod . 
```

The config.yaml file in the root directory is used to define the variables that will be used in the jinja2 templates. The config.yaml file is required for the anomalo-compile command to work.

View the examples directory for examples of how to use the anomalo-compile command and structure your project. 

This uses deepmerge to complile all of the variables but of a higher priority. The order of the files is important. The first file in the list will be the lowest priority and the last file in the list will be the highest priority.