#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load the data from the datasets/salesdata.db database
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
# If you want to know the names of the fields in that table once you have the name, you can change your SQL statement to:
sql = "select * from scores;"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df.head()


# In[3]:


# Load the data from the datasets/salesdata.db database
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
# If you want to know the names of the fields in that table once you have the name, you can change your SQL statement to:
sql = "select * from scores;"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




