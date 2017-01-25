#!/bin/bash

print_usage () {
	printf "Usage: $0 [options] file\n\t-p python\n\t-s sh\n\t-b bash\n\t-h help\n"
	exit 0
}

# Parse options
while getopts :psb opt; do
	case $opt in
		p)
			p=${OPTARG}
		;;
		s)
			s=${OPTARG}
		;;
		b)
			b=${OPTARG}
		;;
		*)
			print_usage
		;;
	esac
done

# Parse file
if [[ $(($# - $OPTIND)) -lt 0 ]]; then
	# No file passed
	echo "No file passed"
	print_usage
fi

f=${@:OPTIND:1}

if [ ! -f $f ]; then
	echo "$f is not a file"
	print_usage
fi

shebang="#!/usr/bin/env python"
if ! [[ -z ${s+x} ]]; then
	shebang="#!/bin/sh"
elif ! [[ -z ${b+x} ]]; then
	shebang="#!/bin/bash"
fi

num_lines="$(cat $f | wc -l)" 2> /dev/null

if [ ${num_lines} -eq 0 ]; then
	echo ${shebang} >> $f
	exit 0
fi

sed -i "1 i${shebang}" $f
