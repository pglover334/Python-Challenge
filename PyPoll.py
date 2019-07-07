# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 17:12:42 2019

@author: User
"""

import csv

list1=[]
with open("C:\\apps\Anaconda36\HW-3 (PyPoll).csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        list1.append(row)
        
del list1[0]
new=[a for a,b,c in list1]
new2=set(new)
answer = len(new2)

print('Total votes: ' + str(answer))

#HW-2

new3=[c for a,b,c in list1]
answer2=set(new3)

print('List of candidates: ' + str(answer2))

#HW-3

answer3={}

for person in answer2:
    for a,b,c in list1:
        if person==c:
            if person not in answer3:
                
                answer3[person] = 1
            else:
                answer3[person] = answer3[person]+1
        
print('Total number of votes per candidate: ' + str(answer3))
                
#HW-4
                
for a,b in answer3.items():
    percentage = (b/len(list1))*100
    answer_1=a
    answer_2=percentage
    print('Percentage of votes: ' + str(answer_1) + ' - %' + str(answer_2)) 

#HW-5

answer4=[]

for a,b in answer3.items():
    answer4.append(b)             

max_1=max(answer4)

for a,b in answer3.items():
    if b==max_1:
        print(a)
        x=a
        print('Winner: ' + x)
        



