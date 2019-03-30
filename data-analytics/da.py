import numpy as np
import pandas as pd

best_members = (pd.read_excel('../dataset/best_members.xlsx'))
large_families = (pd.read_excel('../dataset/large_families.xlsx'))
guardians = (pd.read_excel('../dataset/guardians.xlsx'))
encouragings = (pd.read_excel('../dataset/encouragings.xlsx'))
single_parents_experience = (pd.read_excel('../dataset/single_parents_experience.xlsx'))
registry = (pd.read_excel('../dataset/registry_SKL_DOL.xlsx'))

print("Лучшие сотрудники", best_members.head(), end='\n\n', sep='\n')
for col in best_members.columns: 
    print(col) 
print("Многодетные", large_families.head(), end='\n\n', sep='\n')
for col in large_families.columns: 
    print(col) 
print("Опекуны", guardians.head(), end='\n\n', sep='\n')
for col in guardians.columns: 
    print(col) 
print("Поощрения", encouragings.head(), end='\n\n', sep='\n')
for col in encouragings.columns: 
    print(col) 
print("Родители-одиночки", single_parents_experience.head(), end='\n\n', sep='\n')
for col in single_parents_experience.columns: 
    print(col) 
print("Заявки", registry.head(), end='\n\n', sep='\n')
for col in registry.columns: 
    print(col) 

best_members = (pd.read_excel('../dataset/best_members.xlsx')).dropna()
large_families = (pd.read_excel('../dataset/large_families.xlsx')).dropna()
guardians = (pd.read_excel('../dataset/guardians.xlsx')).dropna()
encouragings = (pd.read_excel('../dataset/encouragings.xlsx')).dropna()
single_parents_experience = (pd.read_excel('../dataset/single_parents_experience.xlsx')).dropna()
registry = (pd.read_excel('../dataset/registry_SKL_DOL.xlsx')).dropna()

df.drop(columns=['B', 'C'])

