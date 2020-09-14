#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load all of the data in the datasets/weekly_call_data folder into one dataframe
import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/weekly_call_data/weekdata*.xlsx"):
 df = pd.read_excel(f)
 all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:




