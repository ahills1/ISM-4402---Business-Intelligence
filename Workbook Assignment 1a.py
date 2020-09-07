#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/all_040_in_12.P1.csv"
df = pd.read_csv(Location)


# In[4]:


df.head()


# In[11]:


import pandas as pd
NAME= ['Florida']
GEOID = [12]
SUMLEV = [40]
STATE = [12]
POP100 = [18801310]
HU100 = [8989580]
POP1002000 = [15982378]
HU1002000 = [7302947]
P001001 = [18801310]
P0010012000 = [15982378]
Degrees = zip(NAME,GEOID,SUMLEV,STATE,POP100,HU100,POP1002000,HU1002000,P001001,P0010012000)
columns = ['NAME','GEOID','SUMLEV','STATE','POP100','HU100','POP1002000','HU1002000','P001001','P0010012000']
df = pd.DataFrame(data = Degrees, columns = columns)


# In[12]:


df.head()


# In[ ]:




