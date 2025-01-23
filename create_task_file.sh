#!/usr/bin/env bash

if [ $# -le 1 ]; then
	echo "incorrect syntax!"
	echo "script.sh <N_OF_MODULE> <NAME>"
	exit 1
fi

TASK_NAME=$(echo "$2" | sed -e 's/ /_/g' | sed -e "s/[.,']//g")

touch "Module_$1/$TASK_NAME.py"

