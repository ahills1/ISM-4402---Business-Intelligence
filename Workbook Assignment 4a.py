#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Pandas and Create Dataframe
import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]

# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']
df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names)
pd.value_counts(df['lettergrade'])
df.head()


# In[5]:


# Create the bin dividers
bins = [0,80,100]

# Create names for the two groups
status_names = ['Fail','Pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins,labels=status_names)
pd.value_counts(df['Pass/Fail'])
df.head()

