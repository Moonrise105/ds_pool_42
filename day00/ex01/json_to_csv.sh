#!/bin/sh
path=${1}
filter=$(cat filter.jq)
cat $path | jq -r "$filter" > hh.csv
