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


# In[7]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)


# In[9]:


get_ipython().run_line_magic('pinfo', 'df.to_csv')


# In[14]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns = columns)
df


# In[16]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns = columns)
df.to_csv('studentgrades.csv',index=False,header=False)


# In[17]:


import pandas as pd
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/gradedata.xlsx"
df = pd.read_excel(Location)


# In[18]:


df.head()


# In[19]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[20]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names','Grades'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[ ]:




