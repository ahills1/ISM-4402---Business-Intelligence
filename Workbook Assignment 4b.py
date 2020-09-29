#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load Data from CSV
import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


#Create the timemgmt column
import numpy as np
df['timemgmt'] = np.where((df['exercise'] > 3) & (df['hours'] > 17),'Busy', 'Not as Busy')
df.head(25)

