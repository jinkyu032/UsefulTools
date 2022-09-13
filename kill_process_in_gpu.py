#!/usr/bin/env python
# coding: utf-8

# In[1]:





import os,sys


# In[2]:


a=range(1,10)


# In[3]:


print(a[0])
a=a[1:]


# In[4]:


import torch
x=torch.rand(10)
print(x)
print(x[:-3])


# In[5]:


import subprocess
import shlex


# In[6]:


x={'1':10,'2':20}
y={'3':30,'4':40}
x.update(y)
print(x)


# In[7]:


subprocess.Popen(['echo','asdf'],stdout=subprocess.PIPE)


# In[8]:


command=shlex.split('nvidia-smi')
print(type(command))
out=subprocess.Popen(command,stdout=subprocess.PIPE) 


# In[9]:


a,b=out.communicate()


# In[10]:


print(a)


# In[11]:


result=a.decode('utf-8')

print(result)


# In[12]:


print(result.split(' '))


# In[13]:


def get_PID(input):
    parsed_by_space_input=input.split(' ')
    x=parsed_by_space_input
    l=len(x)
    result=[]
    find_python=False
    for i in range(l):
        idx=l-1-i
        el=x[idx]
        if 'python' in el:
            find_python=True
            continue
        else:
            if find_python and el.isdigit():
                result.insert(0,el)
                find_python=False
    return result
        


# In[14]:


'abc'.isdigit()


# In[15]:


'12354'.isdigit()


# In[16]:


get_PID(result)


# In[17]:


def kill_PID(input):
    for el in input:
        subprocess.Popen(['kill',el],stdout=subprocess.PIPE) 


# In[18]:


kill_PID(get_PID(result))


# In[ ]:




