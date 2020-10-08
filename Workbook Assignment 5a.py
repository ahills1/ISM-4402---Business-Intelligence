#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Load Dataset from CSV and create Random Sample of 500 Rows from Dataframe
# Import packages
import pandas as pd
import numpy as np
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
# Random Sample of 500 Rows from Dataframe
df.take(np.random.permutation(len(df))[:500])



