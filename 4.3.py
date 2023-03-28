import pandas as pd

df = pd.read_csv('precious_metal.csv', sep=';')

df1 = df.rename(columns ={'GOLDA':'gold', 'Silver':'silver', 'platinu':'platinum', 'Palla':'palladium', 'Date':'date'})
print(df1)

df2 = df1.isnull().sum()
print(df2)

df3 = df1.fillna(0)
print(df3)