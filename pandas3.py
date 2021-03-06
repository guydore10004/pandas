import pandas as pd

#question 1

df_people = pd.read_excel('people.xlsx')
df_animals = pd.read_excel('animals.xlsx')

df1 = df_people.rename(columns={'ID' : 'PersonID' , 'name' : 'PersonName' , 'age' : 'PersonAge'})



#question 2

df2 = df_animals.rename(columns={'ID' : 'AnimalID' , 'Name' : 'AnimalName' , 'Age' : 'AnimalAge'})


#question 3


df3 = df1.merge(df2, left_on='PersonID' , right_on='Owner_ID')



#question 4

df4 = df1.merge(df2, left_on='PersonID' , right_on='Owner_ID' , how='left')


#question 5

df5 = df3['PersonName'].unique()



#question 6

df6 = df3.loc[(df3['PersonName'] == 'Ido')]



#question 7

df7 = df3.loc[(df3['PersonAge'] > 20)]


#question 8

df8 = df3.loc[(df3['PersonAge'] >= 30)]


#question 9

df9 = df3.loc[(df3['Gender'] == 'F') & (df3['Type'] == 'dog') | (df3['Type'] == 'cat')]



#question 10

df10 = df4.loc[(df4['Gender'] == 'M') & (df4['Type'].isnull())]



#question 11

df11 = df3.loc[(df3['Gender'] == 'F') & (df3['Color'] == 'white')]


#question 12

df12 = df3.loc[(df3['Gender'] == 'M') & (df3['Type'] == 'dog') & (df3['PersonAge'] >= 21)]
df12 = df12['Color'].unique()


#question 13

df13 = df10['PersonName']


#question 14

df14 = df3.loc[(df3['Gender'] == 'F') & (df3['Color'] != 'black') & (df3['AnimalAge'] >= 3)]


#question 15

df15 = df3.loc[(df3['AnimalName'] == df3['AnimalName'])]
df15 = df15.AnimalName.value_counts()
df15 = df15[df15 > 1]

#question 16

df16=df3.loc[df3['PersonID']==df3['AnimalID']]
df16=df3['PersonName']

#question 17

#animal gender missing in the chart

#question 18

df18=df1.merge(df2, left_on='Owner_ID' , right_on='PersonID' , how='left')
df18=df18.loc[~(df18['Type'].notnull())]
df18=df18[['AnimalName','AnimalID']]

#question 19

df19=df3['Owner_ID'].value_counts()

#question 20

df20=df3.groupby('Gender')
df20=df20['Owner_ID'].count()

#question 21

df21=df3.sort_values(by='AnimalAge', ascending=False)

#question 22

df22=df21.head(5)

#question 23

df23=df21.loc[~(df21['AnimalName']=='Ido')]
df23=df23.head(12)

#question 24

df24=df3.sort_values(by='AnimalAge')
df24=df24.loc[df24['Color']=='white']

#question 25

df25=df3.sort_values(by='PersonAge',ascending=False)
df25=df25.head()
df25=df25['PersonName']

#question 26

df26=df21.head()
df26=df26['AnimalName']

#question 27

df27=df21.loc[~(df21['PersonName']=='Ido')]
df27=df27.head(12)

#question 28

df28=df21.head(3)
df28=df28['PersonName']

#question 29

df29=df3.groupby('PersonID')
df29=df29['AnimalAge'].max()

#question 30

df30 = df3.sort_values(by=['Age_y'], ascending=False)
df30 = df30.groupby('Type').mean().head(1)
df30 = df30.reset_index()['Type'][0]

