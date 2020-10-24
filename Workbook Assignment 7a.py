#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Import Pandas and Create Dataframe
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])

#Code to Plot my Customized Graph
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

df.plot()
displayText = "WOW!"
#the coordinates of the data point we want to annotate
xloc = 0.0
yloc = 76
#The coordinates of where we want the text to appear
xtext = 200
ytext = 100

#Code to place arrow in graph
plt.annotate(displayText, xy=(xloc, yloc),
     arrowprops=dict(facecolor='black', shrink=0.05),
     xytext=(xtext,ytext),
     xycoords=('axes fraction', 'data'),
     textcoords='offset points')


# In[ ]:




