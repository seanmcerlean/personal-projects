#!/usr/bin/env bash

# Tested on Fedora bash

# Move up N dirs at a time
function up(){ NUM=$1; for i in `seq $NUM`; do cd ..; done }

# Show size of all files under current directory
function dir_size(){ du -h --max-depth 0 `pwd`; }

# Compress / decompress a file to .tgz
function tgz(){ FILE=$1; tar zcvf ${FILE%.*}.tgz $FILE; }
function untgz(){ FILE=$1; tar zxvf $FILE; }

# See open ports for process
function ports(){ PROC=$1; netstat -pan | grep $PROC; }

# Get %CPU Idle
function idle(){ vmstat 1 2 | tail -n 1 | awk '{print $15}'; }

# See all files under cwd which contain STR
function find_str(){ STR=$1 | grep -IRc $STR * | grep -v 0; }


