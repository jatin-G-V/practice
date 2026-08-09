#!/bin/bash
File=$1
count=${2:-10}

tr -cs '[:alpha:]' '\n' < "$File" \
| tr '[:upper:]' '[:lower:]' \
| sort \
| uniq -c \
| sort -nr \
| head -n "$count"