#!/bin/bash

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic \
    --no-input \
    --no-post-process

if [[ -z "$@" ]]
then
    echo "Docker CMD is empty. Please provide one."
else
    # Execute the command passed by CMD
    $@
fi
