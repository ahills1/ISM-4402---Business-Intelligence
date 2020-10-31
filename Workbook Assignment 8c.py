#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Creating a Scatter Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Locates data 
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(Location)
df.head()
#What to plot
df.plot.scatter(x='hours', y='grade')


# In[ ]:




