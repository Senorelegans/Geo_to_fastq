#!/usr/bin/env bash

num=GSE48035


Rscript --verbose GEO.R ${num} > GEO.Rout
python parse.py


