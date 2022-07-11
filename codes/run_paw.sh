#!/bin/bash
for d in */
do
	cd $d
	paw_fast.x ${d::-1}.cntl
	cd ..
done
