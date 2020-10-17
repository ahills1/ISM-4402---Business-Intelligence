#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Pandas and Create Dataframe
import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Sort the dataframe by name, age, and then grade
df=df.sort_values(by=['lname','age','grade'],
                 ascending=[True,True,True])
df.head()


# In[ ]:




