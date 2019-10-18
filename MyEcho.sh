#!/bin/bash

nrep=$1

while [ ${nrep} -gt 0 ]; do
	echo "${nrep} more to go"
	nrep=$(( $nrep - 1 ))
	sleep 2
done
