#!/bin/bash
poetry init -n --name {{cookiecutter.package_name}} --python ^{{cookiecutter.python_version.split('.')[0]}}.{{cookiecutter.python_version.split('.')[1]}}
poetry add --group dev pytest ruff
echo "{{cookiecutter.python_version}}" >> .python-version
echo '
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ssv"
testpaths = [
    "tests",
]

[tool.ruff.lint]
select = ["ALL"]
' >> pyproject.toml
{% if cookiecutter.packages_to_be_installed != "" %}
poetry add {{cookiecutter.packages_to_be_installed}}
{% endif %}
