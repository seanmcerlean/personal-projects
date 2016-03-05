#!/bin/bash

function usage() {
  echo "USAGE: change_filename_char.sh file <options>. Only 1 character can be changed at a time.
  -f File or directories to change. Wildcards can be used for multiple files
  -c The character to change. Defaults to space.
  -n The character to change. Defaults to _
  -r Change filenames recursively, if a directories are included
  "
}

# defaults
OLDCHAR=" "
NEWCHAR="_"
RECURSIVE=1
FILE=''

while getopts c:f:n:r FLAG; do
  case $FLAG in
    c) # Character to change
       OLDCHAR=$OPTARG
       if [ ${#OLDCHAR} -ne 1 ]; then echo "Can only change 1 character at a time."; exit 1; fi
       ;;
    f) # Files to change
       FILE=$OPTARG
       ;;
    n) # Replacement character
       NEWCHAR=$OPTARG
       if [ ${#NEWCHAR} -ne 1 ]; then echo "Can only change 1 character at a time."; exit 1; fi
       ;;
    r) # Recursive change
       RECURSIVE=1000
       ;;
    \?)# Unrecognized option - show help
       echo -e \\n"Option -${BOLD}$OPTARG${NORM} not allowed."
       usage
       exit 1
       ;;
  esac
done

if [ -z "$FILE" ]; then
    echo "At least one file or directory is required"
    usage
    exit 1
fi

find . -depth -maxdepth $RECURSIVE -name "$FILE" |
    while IFS='' read -r fname; do
        if [[ "$fname" == *"$OLDCHAR"* ]]; then
            echo "Moving $fname to $(dirname "$fname")/$(basename "$fname" | tr "$OLDCHAR" "$NEWCHAR")"
            mv -i "$fname" "$(dirname "$fname")/$(basename "$fname" | tr "$OLDCHAR" "$NEWCHAR")"
        fi
    done


