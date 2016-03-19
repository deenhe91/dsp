

with open('emails1.csv', 'w') as csvfile:
    a = csv.writer(csvfile, delimiter = ',')
    for email in email_list:       
        a.writerow([email])
