import numpy as np
import pandas as pd

best_members = (pd.read_excel('../dataset/best_members.xlsx'))
large_families = (pd.read_excel('../dataset/large_families.xlsx'))
guardians = (pd.read_excel('../dataset/guardians.xlsx'))
rewards = (pd.read_excel('../dataset/encouragings.xlsx'))
single_parents_experience = (pd.read_excel('../dataset/single_parents_experience.xlsx'))
registry = (pd.read_excel('../dataset/registry_SKL_DOL.xlsx'))


best_members = best_members.drop(columns=['why', 'data', 'order ', 'subinfo']).dropna()
large_families = large_families.drop(columns=['ind', 'site', 'date_bth', 'Степень родства',
       'ФИ0 ребенка', 'ch_date']).dropna()
guardians = guardians.drop(columns=['ind', 'site', 'date_bth', 'Степень родства',
       'ФИ0 ребенка', 'ch_date']).dropna()
rewards = rewards.drop(columns=['ind', 'site', 'data_dr', 'comand', 'status', 'position',
       'func_code', 'func_name', 'access_date', 'dismisы_date', 'paper',
       'причина', 'причина уточн.', 'Кратко', 'Название ставки', 'Категория',
       'Поощрение От', 'Поощрение До', 'Уточнение', 'Основание']).dropna()
single_parents_experience = single_parents_experience.drop(columns=['site', 'date_bth', 'marital_status']).dropna()

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

with pd.option_context('display.max_rows', 50, 'display.max_columns', 50):
    print("Лучшие сотрудники", best_members, end='\n\n', sep='\n')
    print (best_members.columns)
    print("Многодетные", large_families, end='\n\n', sep='\n')
    print (large_families.columns)
    print("Опекуны", guardians, end='\n\n', sep='\n')
    print (guardians.columns)
    print("Поощрения", rewards, end='\n\n', sep='\n')
    print (rewards.columns)
    print("Родители-одиночки", single_parents_experience, end='\n\n', sep='\n')
    print (single_parents_experience.columns)
    print("Заявки", registry, end='\n\n', sep='\n')
    print (registry.columns)

