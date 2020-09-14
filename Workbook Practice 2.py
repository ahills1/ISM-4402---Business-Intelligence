#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Saving Data to Excel Files
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
 columns=['Names','Grades'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[3]:


# Exporting Multiple Dataframes to Excel
# This assumes that you have another dataframe already loaded into the df2 variable.
# writer = pd.ExcelWriter('dataframe.xlsx',engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet1')
# df2.to_excel(writer, sheet_name='Sheet2')
# writer.save()


# In[6]:


#Export the dataframe created by the code shown below to Excel
import pandas as pd
names = ['Nike','Adidas','New Balance','Puma','Reebok']
prices = [176,59,47,38,99]
PriceList = zip(names,prices)
df = pd.DataFrame(data = PriceList, columns=['Names','Prices'])

writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Shoe_Data')
writer.save()


# In[7]:


df.head()


# In[11]:


#Combining Data from Multiple Excel Files -- the long way
import pandas as pd
import numpy as np
all_data = pd.DataFrame()
df = pd.read_excel("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/data1.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/data2.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/data3.xlsx")
all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[12]:


#Combining Data from Multiple Excel Files -- the short way
import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/data*.xlsx"):
 df = pd.read_excel(f)
 all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[19]:


# load all of the data in the datasets/weekly_call_data folder into one dataframe
import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/weekly_call_data/weekdata*.xlsx"):
 df = pd.read_excel(f)
 all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[21]:


# Load Data from sqlite
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
sql = 'SELECT * from test'
'where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[35]:


# Finding the Table Names
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
#If you don't know the names of the tables in a sqlite database, you can find out by changing the SQL statement to:
sql = "select name from sqlite_master"
"where type = 'table';"
# to find the name of the table
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[39]:


# Finding the Table Names: A Basic Query
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
# If you want to know the names of the fields in that table once you have the name, you can change your SQL statement to that shown:
sql = "select * from scores;"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df.head()


# In[40]:


# Load the data from the datasets/salesdata.db database
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
# If you want to know the names of the fields in that table once you have the name, you can change your SQL statement to that shown:
sql = "select * from scores;"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




