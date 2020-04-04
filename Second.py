#!/usr/bin/env python
# coding: utf-8

# Second

# In[2]:


def fun_depth(t,result,prev):
    if prev != '' and t != '':
        if int(prev) > int(t[0]):
            for i in range(int(prev)-int(t[0])):
                result = result + ')'
    if t == '':
        for i in range(int(prev)):
            result = result + ')'
        return result
    
    #For 0 as first bit
    if int(t[0]) == 0:
        return fun_depth(t[1:],result + t[0],t[0])
    
    #For 1 as first bit
    if int(t[0]) == 1:
        if prev != '':
            if int(prev) == 0:
                result = result + '(' + t[0]
            else:
                result = result + t[0]
        else:
            result = result + '(' + t[0]
        return fun_depth(t[1:],result,t[0])
    
    #Handling for 2 to 9 as first bit
    if int(t[0]) > 1:
        if prev != '':
            for i in range(int(t[0]) - int(prev)):
                result = result + '('
            result = result + t[0]
        else:
            for i in range(int(t[0])):
                result = result + '('
            result = result + t[0]
        return fun_depth(t[1:],result,t[0])
    
#-------Execution starts ----------
#Getting number of test cases
test_case_num = int(input())
for i in range(0,test_case_num):
    s = input()
    print('Case #{}: {}'.format(i + 1,fun_depth(s,'','')))


# In[ ]:




