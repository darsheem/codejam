#!/usr/bin/env python
# coding: utf-8

# Third

# In[2]:


test_case_num=int(input())

def getkey0(item):
    return item[0]
def getkey2(item):
    return item[2]

list1=[]
list2=[]
for i in range(test_case_num):
    n=int(input())
    list1.clear()
    for x in range(n):
        list2=[]
        list2=[int(a) for a in input().split(" ")]
        list2.append(x)
        list1.append(list2)
    list1.sort(key=getkey0)
    cs=-1
    js=-1
    flag=True
    for a in list1:
        ti=a[0]
        ts=a[1]
        if cs==-1:
            cs=ts
            a.append('C')
        elif ti>=cs:
            cs=ts
            a.append('C')
        elif ti<cs and ti>=js:
            js=ts
            a.append('J')
        elif ti<cs and ti<js:
            flag=False
            break
    if flag==False:
        str="IMPOSSIBLE"
    else:
        str=""
        list1.sort(key=getkey2)
        str=str.join([a[3] for a in list1])
    print("Case #{}: {}".format(i+1,str))


# In[ ]:




