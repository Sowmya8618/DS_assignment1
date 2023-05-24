#!/usr/bin/env python
# coding: utf-8

# In[1]:


#basic mathematical operations
import numpy as np
a=np.array([6,7,8])
b=np.array([1,2,3])
#addition
sum=np.add(a,b)
#subtraction
sub=np.subtract(a,b)
#multiplication
mul=np.multiply(a,b)
print("Addition={}\nSubtraction={}\nMultiplication={}".format(sum,sub,mul))


# In[2]:


#data manipulation
import pandas as pd
#filtering rows
data={'a':[6,2,4,9,1,2,7],'b':[7,7,6,3,8,2,1]}
df=pd.DataFrame(data)
print(df)
""""#filtering by column value
df.loc[df['a']==2]"""
# Filter Rows by Logical Conditions
df.loc[df['a']>4]
#concatenating
data1={'a':[6,2,4,9,1,2,7],'b':[7,7,6,3,8,2,1]}
df=pd.DataFrame(data)
data2={'a':[1,2,4,9,1,2,6],'b':[1,7,3,4,5,5,9]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

d=[df1,df2]

print(pd.concat(d))
#merging dataframes
left = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    })
right = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],})
result = pd.merge(left, right, on="key")
print(result)
#summary statistics
data1={'a':[6,2,4,9,1,2,7],'b':[7,7,6,3,8,2,1]}
df=pd.DataFrame(data)
df['a'].mean()
df['a'].median()
df.groupby('a')
df['a'].value_counts()


# In[12]:


import matplotlib.pyplot as plt
#line chart
df=pd.read_csv('diabetes.csv')
x = df['BloodPressure']
y=df['Age']
plt.plot(x, y)
plt.ylabel('Age')
plt.xlabel('BloodPressure')
plt.title("Linear graph")
plt.show()
#bar chart
plt.bar(x, y, color ='maroon',
        width = 0.4)
plt.ylabel('Age')
plt.xlabel('BloodPressure')
plt.title("bar graph")
plt.show()
plt.pie(y)
plt.show()


# In[ ]:




