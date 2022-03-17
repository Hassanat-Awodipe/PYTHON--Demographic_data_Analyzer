import pandas as pd
df = pd.read_csv('adult_data.csv')
#print(df.head()) 

#print(df.columns)

#print(df['race'].value_counts())
#df = df['race'].value_counts()
#df = df.to_frame()
#print(df)

'''df = df['race'].value_counts().to_frame().reset_index()
df.columns = [' race', 'count']
print(df)

value_counts = df['course_difficulty'].value_counts()

# converting to df and assigning new names to the columns
df_value_counts = pd.DataFrame(value_counts)
df_value_counts = df_value_counts.reset_index()
df_value_counts.columns = ['unique_values', 'counts for course_difficulty'] # change column names
df_value_counts'''

#print (df[df['sex']=='Male']['age'].mean().round(1))

#print((df['education'] == 'Bachelors').sum())
#print(len(df['education']))
#print((((df['education'] == 'Bachelors').sum()) / (len(df['education'])) * 100).round(1))

#find the total number of people with advanced education.
#find the no of those who earn more than 50k from the above.
#df1 = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].shape[0]
#print(df1)

#df2 =  df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].shape[0]
#print(df2)

#print(((df2/df1)*100).round(1))

#print(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].shape[0])

#print(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].shape[0])

#print(round(((len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')])) / (len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')])) * 100), 1))



#find the total number of people without advanced education.
#find the no of those who earn more than 50k from the above

#df3 = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].shape[0]
#print(df3)

#df4 = df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')].shape[0]
#print(df4)

#print((df4/df3)*100)

#print(round((((df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')].shape[0]/ df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].shape[0])) * 100), 1))

#print(df['hours-per-week'].min()) 

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?

#number of people who work the min hours
#print(len(df[df['hours-per-week'] == df['hours-per-week'].min()]))

#number of people who earn more than 50k from the above
#print(len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary']== '>50K')]))

print(round((((len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary']== '>50K')])) / (len(df[df['hours-per-week'] == df['hours-per-week'].min()]))) * 100)))

"""min_work_hours = df['hours-per-week'].min()
#print(min_work_hours)

num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
#print(num_min_workers)

rich_percentage = round(
    (((len(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary']== '>50K')])) / 
      (num_min_workers))) * 100)
print(rich_percentage)"""


# What country has the highest percentage of people that earn >50K?

#print(((((df.loc[df['salary']== '>50K']['native-country']).value_counts()) / (df['native-country'].value_counts())) * 100))

#print(((((df[df['salary']== '>50K']['native-country']).value_counts()) / (df['native-country'].value_counts())) * 100).round(1))

'''df = df['race'].value_counts().to_frame().reset_index()
df.columns = [' race', 'count']
print(df)

df4 = ((((df[df['salary']== '>50K']['native-country']).value_counts()) / (df['native-country'].value_counts())) * 100).round(1).to_frame().reset_index()
df4.columns = ['native-country', 'salary>50K_count']
print(df4.head())
print('')
df5 = df4.sort_values(by='salary>50K_count', ascending=False).head(1)
print(df5)
print(df5.iloc[0,0])



#Identify the most popular occupation for those who earn >50K in India.

df = df[(df['native-country']=='India') & (df['salary'] =='>50K')]['occupation'].value_counts().to_frame().reset_index()
df.columns = ['occupation', 'count']
print(df)
df = df['occupation'][0]
print(df)

'''


