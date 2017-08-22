# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:38:14 2017

@author: uka_in
"""

import csv,sys
f = open("SMP 2017 Student Form (Responses) - Sheet2.csv","rb")
f2=open("sorted.txt","w")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
list1_a=[]

for row in reader:
    if row[0] != '' and row[0] !=' ':
        list1_a.append(row[0])
        print "appended"
    pass
f = open("SMP 2017 Student Form (Responses) - Sheet2.csv","rb")
reader = csv.reader(f)
#print list1_a
for row1 in reader:  
    #print "Hello"
    try:
        a= list1_a.index(row1[1])
        #print "Hello"
    except:
        print row1[1]
