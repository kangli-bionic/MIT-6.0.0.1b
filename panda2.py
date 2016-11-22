'''
Step 2 - Working with dataframes
documentation: http://pandas.pydata.org/pandas-docs/stable/
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')

movies.info()
users.describe()
movies.head()
movies.head(10) #default is 5
movies.tail(10)

selectedColumns = users[['age', 'zip_code']].head()

#Users older than 25
print(users[users['age'] > 25].head(3))

#Users 40 and male
print(users[(users['age'] == 40) & (users['sex'] == "M")])

dataNewIndex = users.set_index('user_id')
print(dataNewIndex.head(10))
#users.set_index('user_id', inplace=True) to modify existing dataframe

#Selecting specific row by position
print(dataNewIndex.iloc[8])
print(dataNewIndex.iloc[[99, 100]])

#Select by index
print(dataNewIndex.loc[1])

'''
Joining data:
Like SQL's JOIN clause, pandas.merge allows two DataFrames to be joined on one or more keys.
The function provides a series of parameters (on, left_on, right_on, left_index, right_index)
allowing you to specify the columns or indexes on which to join.
By default, pandas.merge operates as an inner join, which can be changed using the how parameter.
'''

left_frame = pd.DataFrame({'key': range(5),
                           'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7),
                           'right_value': ['f', 'g', 'h', 'i', 'j']})
print(left_frame)
print('\n')
print(right_frame)

print(pd.merge(left_frame, right_frame, on='key', how='inner'))

#pd.merge(left_frame, right_frame, left_on='left_key', right_on='right_key') if different key names

pd.merge(left_frame, right_frame, on='key', how='left')
pd.merge(left_frame, right_frame, on='key', how='right')
pd.merge(left_frame, right_frame, on='key', how='outer')
print(pd.concat([left_frame, right_frame])) #Union all
print(pd.concat([left_frame, right_frame], axis=1)) #Combine data sideways

'''
Grouping
pandas groupby method draws largely from the split-apply-combine strategy for data analysis. If you're not familiar with this methodology,
I highly suggest you read up on it. It does a great job of illustrating how to properly think through a data problem,
which I feel is more important than any technical skill a data analyst/scientist can possess.

When approaching a data analysis problem, you'll often break it apart into manageable pieces,
perform some operations on each of the pieces, and then put everything back together again
(this is the gist split-apply-combine strategy). pandas groupby is great for these problems
'''

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv',
                      header=0,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})
print(chicago.head())
by_dept = chicago.groupby('department')
print(by_dept)
print(by_dept.count().head()) #Total number of non null items in each group
print(by_dept.size().head()) #Total records

print(by_dept.sum().head()) #Aggregate
print(by_dept.title.nunique().sort_values(ascending=False)[:5]) #Count distinct titles by department

'''
Split/Apply/Combine
What if we wanted to see the highest paid employee within each department
'''

def ranker(df):
    """Assigns a rank to each employee based on salary, with 1 being the highest paid.
    Assumes the data is DESC sorted."""

    '''
    This simply adds a range of [1, ... n] for each group
    Using groupby we can define a function (which we'll call ranker) that will label each record from 1 to N,
    where N is the number of employees within the department. We can then call apply to, well,
    apply that function to each group (in this case, each department).
    '''
    df['dept_rank'] = np.arange(len(df)) + 1
    return df

chicago.sort_values('salary', ascending=False, inplace=True)
chicago = chicago.groupby('department').apply(ranker)
print(chicago[chicago.dept_rank == 1].head(7))

print(chicago[chicago.department == 'LAW'][:5])

##25 most rated movies
movie_rating = pd.merge(movies, ratings, on='movie_id', how='inner')
most_rated = movie_rating.groupby('title').size().sort_values(ascending=False)[:5]
print(movie_rating.title.value_counts()[:10]) #Same thing as above
print(most_rated)
#moviesWithRatings = pd.merge(movies, ratingsGrouped, on='movie_id', how='inner')

#Top 25 most highly rated movies
highly_rated = movie_rating.groupby('title').agg({'rating': [np.size, np.mean]}).sort_values([('rating', 'mean')], ascending=False)
print(highly_rated[:25])

atleast_100 = highly_rated['rating']['size'] > 100
print(highly_rated[atleast_100].head())

#Which movies are most controversial between different age groups?

lens = pd.merge(movie_rating, users)

most_50 = lens.groupby('movie_id').size().sort_values(ascending=False)[:50]

users.age.plot.hist(bins=30)
plt.title("Distribution of age groups")
plt.ylabel('Count of users')
plt.xlabel('Age')
#plt.show()

labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
lens['age_group'] = pd.cut(lens.age, range(0, 81, 10), right=False, labels=labels)
print(lens[['age', 'age_group']].drop_duplicates()[:10])

print(lens.groupby('age_group').agg({'rating': [np.size, np.mean]}))

lens.set_index('movie_id', inplace=True)

by_age = lens.loc[most_50.index].groupby(['title', 'age_group'])
print(by_age.rating.mean().head(15))

print(by_age.rating.mean().unstack(1).fillna(0)[:10]) #unstack one makes the age_group into the pivot dimension

#Which movies do men and women disagree most on?
lens.reset_index('movie_id', inplace=True)
pivoted = lens.pivot_table(index=['movie_id', 'title'],
                           columns=['sex'],
                           values='rating',
                           fill_value=0)
print(pivoted.head())
pivoted['diff'] = pivoted.M - pivoted.F
print(pivoted.head())

pivoted.reset_index('movie_id', inplace=True)
disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
disagreements.sort_values().plot(kind='barh', figsize=[9, 15])
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference')
plt.show()
