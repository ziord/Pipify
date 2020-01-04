
# pipify

A simple utility tool for generating requirements.txt files for Python projects.


# Installation
```
git clone https://www.github.com/ziord/pipify.git
cd pipify
python setup.py install
```

# Usage 

```python pipify -P Project_Path```

where ```Project_Path``` is the path to the Python project.


# Issues

This utility tool isn't able to derive accurately 100% of the time, some dependencies that fits installation from PyPI using pip.

You might have to edit the requirements.txt file generated, but only seldomly.
