# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:38:14 2017

@author: uka_in
"""

import csv,sys
f = open("FInal_allocationSMP_2017 - Sheet1.csv","rb")

csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
list1_a=[]

for row in reader:
    if row[6] != '' and row[6] !=' ':
        list1_a.append(row[6].lower())
        print "appended"
    pass
print list1_a
f = open("SMP Mentor Responses - Form Responses 1.csv","rb")
reader = csv.reader(f)
#print list1_a
count =0
for row1 in reader:  
    #print "Hello"
    if row[1] != '' and row[1] !=' ':
        try:
            a= list1_a.index(row1[1].lower())
            #print "Hello"
        except:
            count = count + 1
            print row1[0]+","+row1[1].upper()+","+row1[2]+","+row1[3]+","+row1[4]+","+row1[5]+","+row1[6]+","+row1[7]
print count