#!/bin/bash

FILES=$(mktemp)
for RPM in $(rpm -qa); do
    rpm -ql $RPM | grep "COPYING\|LICENSE" > $FILES
    for FILE in $(cat $FILES); do
	echo $FILE
	cp $FILE notices/$(sha256sum $FILE | awk '{ print $1 }')
    done;
done;

       
			  
