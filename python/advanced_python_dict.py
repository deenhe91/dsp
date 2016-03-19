#DICTIONARIEZ
        
surnames = []
firstnames = []
for name in range(len(faculty)):
    b = faculty.iloc[name,0].split(" ")
    surname = b[-1]
    surnames.append(surname)
    firstname = b[0]
    firstnames.append(firstname)
    
    
new_title_list = []
for title in title_list:
    b = title.split(' of ')
    new_title_list.append(b[0])
    
faculty_dict = {}

#Dictionary one.

for i in range(len(surnames)):
    faculty_dict[surnames[i]] = []

for i in range(len(surnames)):
    if i > 0:
        if surnames[i] != surnames[i-1]:
            faculty_dict[surnames[i]].append([faculty.iloc[i,1], new_title_list[i], email_list[i]])
        else: 
            faculty_dict[surnames[i-1]].append([faculty.iloc[i,1], new_title_list[i], email_list[i] ])
    else:
        faculty_dict[surnames[i]].append([faculty.iloc[i,1], new_title_list[i], email_list[i]])
    
    
for key, value in faculty_dict.items():
    for i in range(3):    
        if key == surnames[i]:
            print (key, ':', value)
    

#Dictionary two.

professor_dict = {}

for i in range(len(surnames)):
    professor_dict[firstnames[i], surnames[i]] = [faculty.iloc[i,1], new_title_list[i], email_list[i]]

for key, value in professor_dict.items():
    for i in range(3):    
        if re.search(surnames[i], str(key)):
            print (key, ':', value)



    
