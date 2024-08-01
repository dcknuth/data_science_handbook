import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

acx = pd.read_csv('acxs22UTF8.csv')
# Let's also put the result in a new column
acx['Age_num'] = acx['Age'].str.extract('(\d+) – (\d+)|<= (\d+)').\
    astype('float').mean(axis=1, skipna=True)
# Bin survey takers by profession
plt.ioff()
sns.set()
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data=acx['Profession'], stat='probability', ax=ax)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Portion of respondents')
plt.show()
# Find the column that applies to hypermobility
for x in acx.columns:
    print(x)
# What are the types of responses?
print(acx['Do you have Ehlers-Danlos or another joint hypermobility syndrome?'].unique())
# Make a column with a shorter name
acx['hypermobile'] = acx['Do you have Ehlers-Danlos or another joint hypermobility syndrome?']
df = acx[['Age_num', 'hypermobile']].dropna()
# Group all the non-No responses to False
df['hypermobileTF'] = df['hypermobile'] == 'No'
g = df.groupby('Age_num')['hypermobileTF'].mean()
# Seem to need some regrouping to get the plot to go
g = pd.DataFrame(g)
g['Age'] = g.index
sns.regplot(x='Age', y='hypermobileTF', data=g)
plt.title("Percent responding No")
plt.show()
# Show the age bins
sns.displot(acx['Age_num'])
plt.show()
