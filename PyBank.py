# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:27:51 2019

@author: User
"""
#----------------------------------------------------------------------------
#PyBank-1

import csv
    
list1=[]
with open("C:\\apps\Anaconda36\HW.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        list1.append(row)
            
del list1[0]
    
for a in list1:
    del a[1]
        
final = []
    
for a in list1:
    month = a[0][:3]
    final.append(month)
    
print('Total distint months: ' + str(len(set(final))))
print('Total months: ' + str(len(final)))
    
#----------------------------------------------------------------------------
#PyBank-2
 
import csv
    
list1=[]
with open("C:\\apps\Anaconda36\HW.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        list1.append(row)
    
del list1[0]
    
new=[int(b) for a,b in list1]
answer=(sum(new))
    
print('Total: $'+ str(answer))

#----------------------------------------------------------------------------
#PyBank-3
    
import csv



list1=[]
with open("C:\\apps\Anaconda36\HW.csv", newline='') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        list1.append(row)

del list1[0]

new=[int(b) for a,b in list1]

new_1=((new[85]-new[0])/len(new))

print('Average change: $' + str(new_1))

#----------------------------------------------------------------------------
#PyBank-4

import csv



list1=[]
with open("C:\\apps\Anaconda36\HW.csv", newline='') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        list1.append(row)
        
del list1[0]  

list2=[]
for a,b in list1:
    list2.append((a,int(b)))
    
new=[b for a,b in list2]

max1=max(new)

for a,b in list2:
    if b==max1:
        print(a,max1)    
    
        answer_1=a
        answer_2=max1

        print('Greatest Increase in Profits: ' + answer_1 + ' $' + str(answer_2))

#----------------------------------------------------------------------------
#PyBank-5

import csv



list1=[]
with open("C:\\apps\Anaconda36\HW.csv", newline='') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        list1.append(row)
        
del list1[0]  

list2=[]
for a,b in list1:
    list2.append((a,int(b)))
    
new=[b for a,b in list2]

min1=min(new)

for a,b in list2:
    if b==min1:
        print(a,min1)
        answer1=a
        
        answer2=min1
        
        print('Greatest Decrease in Profits: ' + answer1 + ' $' + str(answer2))








 