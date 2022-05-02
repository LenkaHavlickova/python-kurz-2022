import pandas as pd
jobs = pd.read_csv("lekce/Lekce09/DataAnalyst.csv", index_col = 0)

print(jobs.columns)
print(jobs.shape)
print(jobs.iloc[10])
# print(jobs.iloc[12:21,6])
print(jobs.iloc[12:21]["Location"])

print(jobs[jobs['Founded']>2000].head())