import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import phik
df = pd.read_csv('ds_salaries.csv')
df.head(15)
df.info()
df.describe()
df.dropna(subset=['salary'], inplace=True) # Удаление строк с пропущенной зарплатой
df['experience_level'] = df['experience_level'].fillna('o') # Заполнение пропусков в столбце "опыт работы"
top_salaries = df.groupby('job_title')['salary'].mean().sort_values(ascending=False)
print(top_salaries.head())
sns.boxplot(x='employee_residence', y='salary', data=df)
plt.show()
sns.scatterplot(x='company_size', y='salary', data=df)
plt.show()
country_stats = df.groupby('company_location').agg({'salary': ['mean', 'median'], 'job_title': 'count'})
country_stats.columns = ['salary', 'median', 'company_size']
country_stats.sort_values(by='company_size', ascending=False, inplace=True)
print(country_stats.head())