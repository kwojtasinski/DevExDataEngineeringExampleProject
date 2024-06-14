#!/bin/bash
set -e
if command -v poetry &> /dev/null
then
    POETRY=poetry
else
    POETRY="/opt/poetry/bin/poetry"
fi
echo "Running ruff check"
$POETRY run ruff check .
