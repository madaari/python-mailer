# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:19:52 2017

@author: uka_in
"""
import csv,sys
f = open("Mentor allocation 2017 SMP - Sheet1.csv","rb")
f2=open("sorted.txt","w")
csv.field_size_limit(sys.maxint)
reader = csv.reader(f)
mentor_name=""
mentor_emailid=""
mentor_phone=""
mentor_roll = ""
stu_email=""
stu_name=""
stu_roll=""
for row in reader:
    print row[1].find("2017U")
    if (row[1].find("2017U")==0):
        pass
        print "Student found"
        stu_email= row[4]
        stu_name= row[0]
        stu_roll= row[1]
        msg=""+stu_email+","+stu_name+","+stu_roll+","+mentor_name+","+mentor_emailid+","+mentor_phone+","+mentor_roll+"\n"
        f2.write(msg)
        print msg
    else:
        print "Mentor found"
        mentor_name=row[0]
        mentor_emailid=row[4]
        mentor_phone=row[3]
        mentor_roll=row[1]
        continue
        
    