#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[2]:


df.head()


# In[3]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/smallgradesh.csv"
df = pd.read_csv(Location)


# In[4]:


df.head()


# In[5]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/smallgradesh.csv"
# To add headers as we load the data...
df = pd.read_csv(Location, names=['Names','Grades'])
# To add headers to a dataframe:
# df.columns = ['Names','Grades']
df.head()


# In[6]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/smallgradesh.csv"
# To add headers as we load the data...
# df = pd.read_csv(Location, names=['Names','Grades'])
# To add headers to a dataframe:
df.columns = ['Names','Grades']
df.head()


# In[ ]:




