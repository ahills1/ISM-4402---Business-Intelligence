#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Creating a Histogram 
#Importing Dataset from CSV File
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
#Categorizing the Histogram by age and gender
df.hist(column="age", by="gender")


# In[ ]:




