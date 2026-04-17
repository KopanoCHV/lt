#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    i=0 #Should start at 0 in order to have the correct index
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
        i+=1 #Makes sure i has the index of the value that head contains
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
            best=mark
        best_idx += 1 #This makes sure that best_idx stores the right index and doesnt remain 0
    return best_idx, best

f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))
