#!/usr/bin/env python
# coding: utf-8

# In[24]:


import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path = HOUSING_PATH):
  if not os.path.isdir(housing_path):
    os.makedirs(housing_path)
  tgz_path = os.path.join(housing_path, "housing.tgz")
  urllib.request.urlretrieve(housing_url, tgz_path)
  housing_tgz = tarfile.open(tgz_path)
  housing_tgz.extractall(path=housing_path)
  housing_tgz.close()


# In[25]:


fetch_housing_data()


# In[26]:


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[27]:


housing = load_housing_data()
housing.head()


# In[28]:


housing.info()


# In[29]:


housing["ocean_proximity"].value_counts()


# In[30]:


housing.describe()


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20, 15))
plt.show()


# In[32]:


from sklearn.model_selection import train_test_split
import numpy as np

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


# In[33]:


test_set.head()


# In[35]:


housing["income_cat"] = pd.cut(housing["median_income"],   
                              bins=[0, 1.5, 3.0, 4.5, 6, np.inf],
                              labels=[1,2,3,4,5])


# In[36]:


housing["income_cat"].hist()


# In[37]:


housing["income_cat"].value_counts()


# In[42]:


from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# In[43]:


strat_test_set["income_cat"].value_counts() / len(strat_test_set)


# In[44]:


for set_ in(strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)


# In[ ]:




