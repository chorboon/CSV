#!/usr/bin/env python3

# We're going to implement a simple CSV parsing function.
# There are two things to focus on. The first (and most importantly)
# is correctly parsing the CSV format. The second is writing
# clean code that another engineer would enjoy using.
#
# You may assume that the CSV file is correctly formatted.
#
# An ideal parse will look like this:
# [['John', 'Smith', 'john.smith@gmail.com', 'Los Angeles', '1'],
# ['Jane', 'Roberts', 'janer@msn.com', 'San Francisco, CA', '0'],
# ['Alexandra "Alex"', 'Menendez', 'alex.menendez@gmail.com', 'Miami', '1'],
# ['1','2','','4','5']]

import csv

csv_list = []
csv_list2 = []

with open('ex.csv') as csv_file:
#    for line in csv.reader(csv_file,quotechar="'", delimiter=','):
#       csv_list.append(line) 
    for line2 in csv_file:
        line2_list = line2.split(',')
        print(line2_list)
        if len(line2) > 5:
            line2_list[3:-2]=[','.join(line2_list[3:-2])]
        line2_list[-1] = line2_list[-1].strip()
        csv_list2.append(line2_list)
        print("ch")



print(csv_list)
print(csv_list2)



