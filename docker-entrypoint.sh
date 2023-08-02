#!/bin/bash

# Apply database migrations
python3 manage.py migrate

if [[ -z "$@" ]]
then
    echo "Docker CMD is empty. Please provide one."
else
    # Execute the command passed by CMD
    $@
fi
