#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#filtering rows
data={'a':[6,2,4,9,1,2,7],'b':[7,7,6,3,8,2,1]}
df=pd.DataFrame(data)
print(df)
""""#filtering by column value
df.loc[df['a']==2]"""
# Filter Rows by Logical Conditions
df.loc[df['a']>4]
#sorting
data={'a':[6,2,4,9,1,2,7],'b':[7,7,6,3,8,2,1]}
df=pd.DataFrame(data)
df.sort_values(by='a')
#aggregating
df = pd.DataFrame([[1, 2, 3],[4, 5, 6],[7, 8, 9]],
                  columns=['A', 'B', 'C'])
df.agg(['sum','min'])


# In[ ]:


# importing libraries
import matplotlib.pyplot as plt
import seaborn
data = [44, 45, 40, 41, 39]
keys = ['Class 1', 'Class 2', 'CLass 3', 'Class 4', 'Class 5']
# define Seaborn color palette to use
#palette_color = seaborn.color_palette('bright')
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
plt.show()
import seaborn
fmri = seaborn.load_dataset("fmri")
seaborn.scatterplot(x="timepoint",y="signal",data=fmri)
import seaborn
fmri = seaborn.load_dataset("fmri")
seaborn.barplot(x="timepoint",y="signal",data=fmri)
plt.show()


# In[ ]:


#Load the required libraries
import pandas as pd
import numpy as np
df = pd.read_csv('diabetes.csv')
df.head()
df.describe()
df.info()
df.duplicated()


# In[ ]:


In Machine Learning, the model requires a dataset to operate, i.e. to train and test. But data doesn’t come fully prepared and ready to use. There are discrepancies like “Nan”/ “Null” / “NA” values in many rows and columns. Sometimes the data set also contains some of the row and columns which are not even required in the operation of our model. In such conditions, it requires proper cleaning and modification of the data set to make it an efficient input for our model. We achieve that by practicing “Data Wrangling” before giving data input to the model.

