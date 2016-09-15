#!/bin/sh

if [ "$#" -ne 1 ]; then
	echo 'Please pass a file as the only argument' >&2
	exit 1
fi 

python_shebang="#!/usr/bin/env python"
num_lines="$(cat $1 | wc -l)"

if [ ${num_lines} -eq 0 ]; then
	echo ${python_shebang} >> $1
	exit 0
fi

sed -i "1 i${python_shebang}" $1
