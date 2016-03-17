#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

import pandas as pd

import numpy as np

def read_data(data):
  	file_obj = open(data)
  	csv_file = pd.read_csv(file_obj)
  	return csv_file

football = read_data('football.csv')
football = football.set_index('Team')

print(football)

# df.set_index('head0') to reassign a column to row names
# i.e. football = football.set_index('Team')
  		

#col1 and col2 must be ints..

def get_min_score_difference(parsed_data, col1, col2):
    goal_dict = {}
    for row in range(len(parsed_data)):
        difference = int(parsed_data.iloc[row, col1]) - int(parsed_data.iloc[row, col2])
        goal_dict[parsed_data.index[row]] = abs(difference)
    return goal_dict


goals_dict = get_min_score_difference(football, 4, 5)

print(goals_dict)


def get_team(parsed_data, parsed_dict):
    
    # make list of absolute value goals.
    goals_list = []
    for i in range(len(parsed_data)):
        a = parsed_dict.get(parsed_data.index[i])
        goals_list.append(a)
    
    team_goals = min(goals_list)
    print('min difference: ' + str(team_goals))
    
    for team in parsed_dict:
        if parsed_dict[team] == team_goals:
            print(team)

get_team(football, goals_dict)

