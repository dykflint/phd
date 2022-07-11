#!/bin/bash
for d in */
do
	cp -- "run0.cntl" "$d${d::-1}.cntl"
done
