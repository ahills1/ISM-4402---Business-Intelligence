#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Dataset from CSV File
import pandas as pd
import matplotlib.pyplot as plt
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv"
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(Location)
df.head(15)


# In[64]:


# 1. Average cars sold per month
df['Cars Sold'].mean()


# In[5]:


# 2. Max cars sold per month
df['Cars Sold'].max()


# In[6]:


# 3. Min cars sold per month
df['Cars Sold'].min()


# In[10]:


# 4. Average cars sold per month by gender
pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[13]:


# 5. Average hours worked by people selling more than three cars per month
df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[14]:


# 6. Average years of experience
df['Years Experience'].mean()


# In[18]:


# 7. Average years of experience for people selling more than three cars per month
df[df['Cars Sold']>3]['Years Experience'].mean()


# In[21]:


# 8. Average cars sold per month sorted by whether they have had sales training
pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[57]:


# Histogram Visualizations
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv"
df = pd.read_csv(Location)
# Create histogram by Cars Sold and if the individual had Sales Training or not
df.hist(column="Cars Sold", by="SalesTraining", color='pink')
# Create histogram by Cars Sold and whether the individual was Male or Female
df.hist(column="Cars Sold", by="Gender", color= 'teal')


# In[74]:


# Bar gragh Visualization
plt.figure(figsize=(8,8), dpi=85)
df_axis_data=pd.read_csv('/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv')
# Create Bar Graph showing Years Experience(x) by Cars Sold(y)
plt.bar(x=df_axis_data['Years Experience'],
  height=df_axis_data['Cars Sold'], color='purple')
plt.xlabel("Years Experience")
plt.ylabel("Cars sold")
plt.title("Bar Visualization")


# In[75]:


# Scatterplot Visualization
plt.figure(figsize=(8,8), dpi=85)
df_axis_data=pd.read_csv('/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv')
# Create Scatter Plot showing Hours Worked(x) by Cars Sold(y)
plt.scatter(x=df_axis_data['Cars Sold'],
  y=df_axis_data['Hours Worked'], color='orange')
plt.xlabel("Cars Sold")
plt.ylabel("Hours Worked")
plt.title("Scatter Plot Visualization")


# In[77]:


# Creating Histograms from axisdata.csv
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.hist()


# In[99]:


# Box Plot Visualization
Location = "/Users/ashle/OneDrive/Documents/USF/ISM 4402- Business Intelligence/datasets/datasets/axisdata.csv"
df = pd.read_csv(Location)
# Create Boxplot based off Sales Training(x) and Cars Sold(y)
axis= df.boxplot(by= 'SalesTraining', column='Cars Sold', color= 'red')
axis.set_ylim(0,8)
plt.xlabel("Sales Training")
plt.ylabel("Cars Sold")


# In[ ]:




