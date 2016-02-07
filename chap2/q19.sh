#!/usr/bin/env bash

cat hightemp.txt | cut -f1 | sort | uniq -c | sort -k 1,1 -r