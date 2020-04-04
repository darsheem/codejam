#!/usr/bin/env python
# coding: utf-8

# First

# In[6]:


sumd = []
row = []
col = []
#Getting number of test cases
test_case_num = int(input())

#Checking for limits
if(1<=test_case_num and 100>=test_case_num):
   
    for i in range(0,test_case_num):
        in_row = 0
        in_col = 0
        trace = 0
        matrix = []
        
        #getting size of matrix
        N = int(input())
        if(2<=N and 100>=N):
            for j in range(N):
                #Getting elements and splitting it by space
                x=input().split(" ")
                a=[]
                for q in range(0,N):
                        #appending elements index wise to the array
                        a.append(int(x[q]))
                #Creating a set in order to remove duplicates
                b = set(a)
                #if length of both varies means duplicate
                if(len(b)!=N):
                    in_row = in_row + 1
                b.clear()
                matrix.append(a)

            #To calculate sum of diagonals 00,11,22,...
            for m in range(0, N):  
                for n in range(0, N):
                    if (m == n):
                        trace = trace+matrix[m][n]
           
            for m in range(0, N):
                co = set()
                for n in range(0, N):
                    #column wise checking of repeating elements
                    co.add(matrix[n][m])
                if(len(co)!=N):
                    in_col = in_col + 1
                co.clear()

        sumd.append(trace)
        row.append(in_row)
        col.append(in_col)
       
    for i in range(test_case_num):
        print("Case #{0}: {1} {2} {3}".format(i+1,sumd[i],row[i],col[i]))

