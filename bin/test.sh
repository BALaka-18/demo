#!/bin/bash

echo -n "Did you install pre-commit ?(1=Y/0=N) "
read ans

if [[ $ans -gt 1 ]]
then
    echo "Go ahead and commit the staged changes."

else
    echo "Install pre-commit first(COMMAND : $ pre-commit install)."
fi
