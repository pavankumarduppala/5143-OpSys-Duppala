#!/bin/bash
#cp $1
x=$(date +%F)
myvar=$x"_$1"
cp $1 $myvar
echo details of filecopied
ls -l $myvar
