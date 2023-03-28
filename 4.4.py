import pandas as pd

df = pd.read_csv('precious_metal.csv', sep=';')

df = df.rename(columns ={'GOLDA':'gold', 'Silver':'silver', 'platinu':'platinum', 'Palla':'palladium', 'Date':'date'})
#print(df)

def replace_symbol(x):
    x = str(x)
    x = float(x.replace(',','.'))
    return x 

df['gold'] = df['gold'].apply(replace_symbol)
df['silver'] = df['silver'].apply(replace_symbol)
df['platinum'] = df['platinum'].apply(replace_symbol)
df['palladium'] = df['palladium'].apply(replace_symbol)

print(df)