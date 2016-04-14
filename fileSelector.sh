#!/bin/bash

ls ~/Desktop/HW/calcheck1 | cut -c4-12 | while read line
do
find ~/Desktop/HW/bss1 -name "*"$line"*" -exec cp {} ~/Desktop/HW/bss \;
done

ls ~/Desktop/HW/bss | cut -c4-12 | while read line
do
find ~/Desktop/HW/calcheck1 -name "*"$line"*" -exec cp {} ~/Desktop/HW/calcheck \;
done
