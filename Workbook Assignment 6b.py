#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Pandas and Create Dataframe
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm

Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)

#Create a new column and convert gender to numeric values (Male = 0, Female = 1)
1 for female and 0 for male
df['genderBool'] = np.where((df['gender'] == "male"),'0', '1')
df.head()

result = sm.ols(
    formula='grade ~ gender + exercise + hours'
    ,data=df).fit()
result.summary()


# In[ ]:




