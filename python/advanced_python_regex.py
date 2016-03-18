PLACE YOUR CODE HERE
import re
import csv
import pandas as pd
import numpy as np

def read_data(data):
  file_obj = open(data)
  csv_file = pd.read_csv(file_obj)
  return csv_file

faculty = read_data('faculty.csv')

degrees = faculty.iloc[:,1]

degree_list = degrees.tolist()

degree_types = ['Ph.D|PhD', 'MD|M.D', 'Sc.D|ScD', 'MS|M.S', 'MA', 'MPH', 'JD', 'B.S|BS']

for x in degree_types:
    d_list = []
    for i in range(len(degree_list)):
        if re.search(x, degree_list[i]):
            d_list.append(degree_list[i])
    print(x + ' count: ' + str(len(d_list)))
    

titles = faculty.iloc[:, 2]
title_list = titles.tolist()
title_set = set(title_list)

for x in title_set:
    t_list = []
    for i in range(len(title_list)):
        if re.search(x, title_list[i]):
            t_list.append(x)
    print(x + ' count:' + str(len(t_list)))
    

# EMAIL ADDRESSES 

emails = faculty.iloc[:,3]

email_list = emails.tolist()

domains = []

for email in emails:
    d = email.split('@')
    domain = d[1]
    domains.append(domain)

unique_domains = set(domains)
    
