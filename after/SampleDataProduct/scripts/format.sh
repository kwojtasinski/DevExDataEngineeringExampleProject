#!/bin/bash
set -e
if command -v poetry &> /dev/null
then
    POETRY=poetry
else
    POETRY="/opt/poetry/bin/poetry"
fi
echo "Running ruff format"
$POETRY run ruff format .
echo "Running ruff fix"
$POETRY run ruff check . --fix
