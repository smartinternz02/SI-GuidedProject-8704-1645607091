#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


t1=sns.load_dataset('tips')
t1


# In[3]:


t1.head()


# In[4]:


plt.plot(t1['total_bill'],)


# In[5]:


sns.lineplot(x='total_bill',y='tip',data=t1,)


# In[6]:


plt.scatter(x='total_bill',y='tip',data=t1)


# In[7]:


sns.scatterplot(x='total_bill',y='tip',data=t1)


# In[39]:


sns.barplot(x='tip',y='total_bill',data=t1.head(30))


# In[9]:


plt.hist(t1['size'])


# In[10]:


sns.histplot(x='tip',data=t1)


# In[11]:


sns.countplot(x='smoker',data=t1)


# In[12]:


sns.get_dataset_names()


# In[13]:


t2=sns.load_dataset('titanic')


# In[14]:


t2


# In[15]:


t2.head()


# In[16]:


t2.corr()


# In[17]:


sns.heatmap(t2.corr())


# In[18]:


sns.boxplot(x='embarked',y='fare',data=t2)


# In[19]:


sns.pairplot(t1)


# In[20]:


t3=sns.load_dataset('exercise')


# In[21]:


t3


# In[22]:


t3.head()


# In[41]:


sns.jointplot(x='pulse',y='id',data=t3,kind='reg')


# In[24]:


sns.kdeplot(x='pulse',data=t3)


# In[25]:


sns.distplot(t2['fare'],bins=30)


# In[ ]:





# In[ ]:




