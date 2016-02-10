#!/bin/bash
x=$(date +%F)
arg=$1
name=$(echo $1|echo "${arg%%.*}")
ext=$(echo $1|cut -d'.' -f2)
newfile=$name"_"$x"."$ext
echo $newfile
cp $1 newfile
echo details of newfile
ls -l $newfile
