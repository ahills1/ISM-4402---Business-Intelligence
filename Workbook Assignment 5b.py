#!/usr/bin/env python
# coding: utf-8

# In[2]:


# creating a dataframe and computing summary statistics using the dataset
# Import packages
import pandas as pd
#Creating Dataset for Statistics
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
# Create Data Frame
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS Degrees','MS Degrees','PhD Degrees'])
df


# In[3]:


# number of values
df['Grades'].count()


# In[4]:


# arithmetic average
df['Grades'].mean()


# In[5]:


# standard deviation
df['Grades'].std()


# In[6]:


# minimum
df['Grades'].min()


# In[7]:


# maximum
df['Grades'].max()


# In[13]:


# first quartile 
df['Grades'].quantile(.25)


# In[11]:


# second quartile
df['Grades'].quantile(.5)


# In[10]:


# third quartile
df['Grades'].quantile(.75)

