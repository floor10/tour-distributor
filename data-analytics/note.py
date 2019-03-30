#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from datetime import datetime


# In[2]:


origins_best_members = (pd.read_excel('../dataset/best_members.xlsx'))
origins_large_families = (pd.read_excel('../dataset/large_families.xlsx'))
origins_guardians = (pd.read_excel('../dataset/guardians.xlsx'))
origins_rewards = (pd.read_excel('../dataset/encouragings.xlsx'))
origins_single_parents_experience = (pd.read_excel('../dataset/single_parents_experience.xlsx'))
origins_registry = (pd.read_excel('../dataset/registry_SKL_DOL.xlsx'))


# In[3]:


best_members = origins_best_members.drop(columns=['why', 'data', 'order ', 'subinfo']).dropna()
large_families = origins_large_families.drop(columns=['ind', 'site', 'date_bth', 'Степень родства',
       'ФИ0 ребенка']).dropna()
guardians = origins_guardians.drop(columns=['ind', 'site', 'date_bth', 'Степень родства',
       'ФИ0 ребенка', 'ch_date']).dropna()
rewards = origins_rewards.drop(columns=['ind', 'site', 'data_dr', 'comand', 'status', 'position',
       'func_code', 'func_name', 'access_date', 'dismisы_date', 'paper',
       'причина', 'причина уточн.', 'Кратко', 'Название ставки', 'Категория',
       'Поощрение От', 'Поощрение До', 'Уточнение', 'Основание']).dropna()
single_parents_experience = origins_single_parents_experience.drop(columns=['site', 'date_bth', 'marital_status']).dropna()
registry = origins_registry.copy()


# In[4]:


best_members.head()


# In[5]:


_dataset = [best_members, large_families, guardians, rewards, single_parents_experience, registry]
dataset = []
for data in _dataset:
    data.drop(data[data.id == 1].index, inplace=True)
    data.drop(data[data.name == 'a'].index, inplace=True)
    data.drop(data[data.name == 'а'].index, inplace=True)
    dataset.append(data)

best_members = dataset[0]
large_families = dataset[1]
guardians = dataset[2]
rewards = dataset[3]
single_parents_experience = dataset[4]
registry = dataset[5]

# In[12]:


large_families.head()


# In[13]:


def how_years_old(date):
    my_date = datetime.strptime(date, '%d.%m.%Y').date()
    now_date = datetime.today().date()
    hash = now_date.year - my_date.year + 0.1*(now_date.month - my_date.month) + 0.01*(now_date.day - my_date.day)
    return hash


# In[14]:


inds_of_adult = []
for i, date in enumerate(large_families.ch_date):
    if (how_years_old(date) >= 18):
        inds_of_adult.append(i)
inds_of_adult[:20]


# In[15]:


large_families = large_families.reset_index()
large_families = large_families.drop(inds_of_adult)
large_families.head()
