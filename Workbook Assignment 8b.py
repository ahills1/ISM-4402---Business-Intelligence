#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Pie Charting the Dataset
import pandas as pd
import matplotlib.pyplot as plt

#Setting up the data set
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]

GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df

#Creating New Column
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df

#Creating the Pie Chart 
plt.pie(df['TotalDemerits'],
 labels=df['Names'],
 explode=(0,0,0,0.30,0),
 startangle=90,
 autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[ ]:




