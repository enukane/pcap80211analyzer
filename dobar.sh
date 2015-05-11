#!/bin/sh

FNAME=`basename $1`
cat $1 | ./charter -o graph/$FNAME.png -t bar
