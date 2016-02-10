#!/bin/bash
path=/usr/share/dict/words
size=$(wc -l < $path)
let mod=$(($RANDOM%size))
line=$(expr $mod + 1)
sed -n {line}p ${path}
