#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:19:47 2024

@author: pato
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/pato/Downloads/DARA/DARA2024/movie_dataset.csv')


#print(df)

#Checking missing values
print('\n\n Checking missing values \n\n', df.isnull().sum())

#Correcting missing values
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median(), inplace=True)
df['Metascore'].fillna(df['Metascore'].median(), inplace=True)

#Checking missing values after correction
print('\n\n Checking missing values after correction \n\n', df.isnull().sum())

#The highest rated movie
highest_rated_movie = df.loc[df['Rating'].idxmax(), ['Title', 'Rating']]
print('\n\n' f"The highest rated movie = {highest_rated_movie['Title']}, Rating: {highest_rated_movie['Rating']}")

#The average revenue of all movies
average_revenue = df['Revenue (Millions)'].mean()
print('\n\n' f"The average revenue of all movies = {average_revenue:.2f} Million")

#The average revenue of movies from 2015 to 2017
movies_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = movies_2015_2017['Revenue (Millions)'].mean()
print('\n\n' f"The average revenue of movies from 2015 to 2017 = {average_revenue_2015_2017:.2f} Million")

#The movies released in the year 2016
movies_2016_count = df[df['Year'] == 2016].shape[0]
print('\n\n' f"The movies released in the year 2016 = {movies_2016_count}")

#The movies directed by Christopher Nolan 
C_nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]
print('\n\n' f"The movies directed by Christopher Nolan = {C_nolan_movies_count}")

#The movies in the dataset having a rating of at least 8.0
highest_rated_movie_atleast_8 = df[df['Rating'] >= 8.0].shape[0]
print('\n\n' f"The movies in the dataset having a rating of at least 8.0 = {highest_rated_movie_atleast_8}")

#The median rating of movies directed by Christopher Nolan
C_nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating = C_nolan_movies['Rating'].median()
print('\n\n' f"The median rating of movies directed by Christopher Nolan = {median_rating}")

#The year with the highest average rating
average_ratings_per_year = df.groupby('Year')['Rating'].mean()
highest_avg_rating_year = average_ratings_per_year.idxmax()
print('\n\n' f"The year with the highest average rating = {highest_avg_rating_year}")

#The percentage increase in number of movies made between 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print('\n\n' f"The percentage increase in number of movies made between 2006 and 2016 = {percentage_increase:.2f}%")

#The most common actor in all the movies
all_actors = df['Actors'].str.split(',').explode().str.strip()
target_actors = ['Matthew McConaughey', 'Chris Pratt', 'Bradley Cooper', 'Mark Wahlberg']
filtered_actors = all_actors[all_actors.isin(target_actors)]
most_common_actor = filtered_actors.value_counts().idxmax()
print('\n\n' f"The most common actor in all the movies = {most_common_actor}")

#Unique genres
all_genres = df['Genre'].str.split(',').explode().str.strip()
unique_genre_count = len(all_genres.unique())
print('\n\n' f"Unique genres = {unique_genre_count}")


'''
Creating plots for correlation of numerical values
'''
# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Runtime (Minutes)', y='Rating', data=df)

# Add a regression line
sns.regplot(x='Runtime (Minutes)', y='Rating', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Rating vs Runtime')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Rating')
plt.savefig('figures/Rating vs Runtime')
plt.show()
#print('1. Rating increases with increase in runtime. However most of the movies have runtime between 90 to 120 minutes and have rating above 5.')


# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Rating', data=df)

# Add a regression line
sns.regplot(x='Votes', y='Rating', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Rating vs Votes')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.savefig('figures/Rating vs Votes')
plt.show()
#print('2. Rating increases with votes. Most of the movies have votes less than 500 000.')



# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Revenue (Millions)', data=df)

# Add a regression line
sns.regplot(x='Votes', y='Revenue (Millions)', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Revenue (Millions) vs Votes')
plt.xlabel('Votes')
plt.ylabel('Revenue (Millions)')
plt.savefig('figures/Revenue (Millions) vs Votes')
plt.show()
#print('3. Revenue seems to increase with votes though the relationship is not strong. Most of the movies with less than 500 000 votes have revenue less than 200 millions.')



# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Metascore', y='Rating', data=df)

# Add a regression line
sns.regplot(x='Metascore', y='Rating', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Rating vs Metascore')
plt.xlabel('Metascore')
plt.ylabel('Rating')
plt.savefig('figures/Rating vs Metascore')
plt.show()
#print('4. Rating strongly relates with metascore.')



# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Runtime (Minutes)', y='Metascore', data=df)

# Add a regression line
sns.regplot(x='Runtime (Minutes)', y='Metascore', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Metascore vs Runtime (Minutes)')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Metascore')
plt.savefig('figures/Metascore vs Runtime (Minutes)')
plt.show()
#print('5. There is no clear relationship between runtime and metascore and it is very weak to almost constant.')



# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Runtime (Minutes)', y='Votes', data=df)

# Add a regression line
sns.regplot(x='Runtime (Minutes)', y='Votes', data=df, scatter=False, color='red', line_kws={'linewidth': 1})

# Labeling
plt.title('Votes vs Runtime (Minutes)')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Votes')
plt.savefig('figures/Votes vs Runtime (Minutes)')
plt.show()
#print('6. Votes depend weakly on runtime.')


print('\n\n Insights deduced are:\n')
print('1. Rating increases with increase in runtime. However most of the movies have runtime between 90 to 120 minutes and have rating above 5.')
print('2. Rating increases with votes. Most of the movies have votes less than 500 000.')
print('3. Revenue seems to increase with votes though the relationship is not strong. Most of the movies with less than 500 000 votes have revenue less than 200 millions.')
print('4. Rating strongly relates with metascore.')
print('5. There is no clear relationship between runtime and metascore and it is very weak to almost constant.')
print('6. Votes depend weakly on runtime.')

print('\n Generally most of highly rated movies have runtime between 90 to 120 minutes.The directors shoud produce movies with runtime within that range of time.')