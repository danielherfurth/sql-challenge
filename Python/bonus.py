import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import password
from sqlalchemy import create_engine

# TODO uncomment below before p2j
# %matplotlib inline

engine = create_engine(
    f'postgresql://postgres:{password}@localhost:5432/sql-challenge'
)

conn = engine.connect()

# read the salaries
salaries_df = pd.read_sql('SELECT * FROM salaries', conn)

# most common salaries
fig = plt.figure(figsize=(12, 8))

# hist with only 10 bins so it's easier to read
ax = sns.histplot(
    salaries_df.salary,
    bins=10
)

# setting labels
ax.set(
    xlabel='Salary ($)',
    title='Salary Distribution'
)

# set vertical line at avg salary
plt.axvline(
    salaries_df.salary.mean(),
    color='black',
    ls='--'
).set_label('Average Salary')

plt.legend()

plt.savefig('Python/salary_dist.png', dpi=200)

# bar chart of average salary by title
# sql query string
query = 'SELECT ROUND(AVG(salary), 2), t.title \
         FROM salaries S \
                JOIN employees e ON S.emp_no = e.emp_no \
                JOIN titles t ON e.title_id = t.title_id \
         GROUP BY t.title_id'

# read the query output into a dataframe
salary_dept = pd.read_sql(
    query,
    conn
)

# give columns better names
salary_dept.columns = ['avg_salary', 'department']

fig = plt.figure(figsize=(12, 8))

ax = sns.barplot(
    x='department',
    y='avg_salary',
    data=salary_dept,
    palette='viridis'
)

ax.set(
    xlabel='Department',
    ylabel='Average Salary ($)',
    title='Average Salary by Department'
)

# rotate ticks and clean up layout
ax.set_xticklabels(ax.get_xticklabels(), rotation=-45)
plt.tight_layout()

# save fig
plt.savefig('Python/avg_salary', dpi=200)

