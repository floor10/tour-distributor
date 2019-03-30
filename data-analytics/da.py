import numpy as np
import pandas as pd

best_members = pd.read_excel('../dataset/best_members.xlsx')
large_families = pd.read_excel('../dataset/large_families.xlsx')
guardians = pd.read_excel('../dataset/guardians.xlsx')
encouragings = pd.read_excel('../dataset/encouragings.xlsx')
single_parents_experience = pd.read_excel('../dataset/single_parents_experience.xlsx')

registry = pd.read_excel('../dataset/registry_SKL_DOL.xlsx')

print(registry.head(), end='\n\n')
print(best_members.head(), end='\n\n')
print(large_families.head(), end='\n\n')
print(guardians.head(), end='\n\n')
print(encouragings.head(), end='\n\n')
print(single_parents_experience.head(), end='\n\n')


