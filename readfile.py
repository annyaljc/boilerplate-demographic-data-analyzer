import pandas as pd
df=pd.read_csv('adult.data.csv')
#print(df['race'].value_counts())

highest_earning_country = (df[df['salary']=='>50K']['native-country'].value_counts()/df['native-country'].value_counts()).idxmax()


highest_earning_country_percentage = df[df['native-country']==highest_earning_country].shape[0]
highest_earning_country_percentage = df[(df['native-country']==highest_earning_country)&(df['salary']=='>50K')].shape[0]
print(highest_earning_country_percentage)