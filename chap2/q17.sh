#!/usr/bin/env bash

cat hightemp.txt | cut -f1 | sort | uniq