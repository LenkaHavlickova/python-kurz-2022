# https://stage.kodim.cz/kurzy/python-data-1/python-pro-data-1/nacteni-dat
# https://pandas.pydata.org/pandas-docs/stable/
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
import pandas as pd
nakupy = pd.read_csv('lekce/Lekce09/nakupy.csv')
# print(nakupy)
# nakupy.info()
# print(nakupy.shape)
# print(nakupy.columns)
# print(nakupy.iloc[3])
# print(nakupy.iloc[0:5])
# print(nakupy.iloc[5:])
# print(nakupy.iloc[-1])
# print(nakupy.iloc[0,0])
# print(nakupy.iloc[:5,[0,3]])
# print(nakupy.iloc[5,1])
# print(nakupy.iloc[:,2])

# print(nakupy.head())
print(nakupy.tail())