#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


fetch_housing_data()


# In[4]:


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[5]:


housing = load_housing_data()
housing.head()


# In[6]:


housing.info()


# In[7]:


housing["ocean_proximity"].value_counts()


# In[8]:


housing.describe()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()


# In[11]:


from sklearn.model_selection import train_test_split
import numpy as np

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


# In[12]:


test_set.head()


# In[13]:


housing["income_cat"] = pd.cut(housing["median_income"],
                              bins=[0, 1.5, 3.0, 4.5, 6, np.inf],
                              labels=[1, 2, 3, 4, 5])


# In[14]:


housing["income_cat"].hist()


# In[15]:


housing["income_cat"].value_counts()


# In[16]:


from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# In[18]:


strat_test_set["income_cat"].value_counts() / len(strat_test_set)


# In[19]:


for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)


# In[23]:


housing = strat_train_set.copy()


# In[25]:


housing.plot(kind="scatter", x="longitude", y="latitude")


# In[26]:


housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)


# In[28]:


housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
            s=housing["population"]/100, label="population", figsize=(10, 7),
            c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
            sharex=False)
plt.legend()


# In[29]:


corr_matrix = housing.corr()


# In[30]:


corr_matrix["median_house_value"].sort_values(ascending=False)


# In[33]:


from pandas.plotting import scatter_matrix

attributes = ["median_house_value", "median_income", "total_rooms",
             "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))


# In[34]:


housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]


# In[35]:


corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)


# In[36]:


sample_incomplete_rows = housing[housing.isnull().any(axis=1)].head()
sample_incomplete_rows


# In[37]:


sample_incomplete_rows.dropna(subset=["total_bedrooms"])


# In[38]:


sample_incomplete_rows.drop("total_bedrooms", axis=1)


# In[39]:


median = housing["total_bedrooms"].median()
sample_incomplete_rows["total_bedrooms"].fillna(median, inplace=True)


# In[40]:


sample_incomplete_rows


# In[41]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")


# In[42]:


housing_num = housing.drop("ocean_proximity", axis=1)


# In[43]:


imputer.fit(housing_num)


# In[44]:


imputer.statistics_


# In[45]:


housing_num.median().values


# In[46]:


X = imputer.transform(housing_num)


# In[47]:


housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                         index=housing_num.index)


# In[49]:


housing_cat = housing[["ocean_proximity"]]
housing_cat.head(10)


# In[50]:


from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
housing_cat_encoded[:10]


# In[52]:


ordinal_encoder.categories_


# In[53]:


from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_cat_1hot


# In[54]:


housing_cat_1hot.toarray()


# In[55]:


cat_encoder.categories_

