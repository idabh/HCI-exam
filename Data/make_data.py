# This script randomly autogenerates a pool of job applications distinguished by a number of different factors

import random
import csv
import names
from os import listdir
from os.path import isfile, join

nr_applicants = 250 # set nr of applicants you want to generate

# set possible variable values (ADD MORE / CHECK THIS!)
sexes = ['female', 'male', 'nonbinary', 'prefer not to say']
edu_levels = ['high school', 'bachelor', 'masters', 'phd']
faculties = ['arts', 'sciences', 'engineering']
education = ['Information Sciences', 'Computer Scientist', 'Software Engineer', 'Media Science', 'Cognitive Science', 'Journalist']

words = ['this ', 'is ', 'a ', 'random ', 'selection ', 'of ', 'words ', 'yay ', 'banana ', 'cool ', 'hello ']
#Hobbies =['Hiking', 'football', 'Gaming', 'Skydiving']
#skills =['communication', 'leadership', 'cooking']
images = [f for f in listdir('Images') if isfile(join('Images', f))]

# create a csv file named to contain the dataset
with open('Data/applicants' + str(nr_applicants) + '.csv', 'w', newline ='') as f: 
    file = csv.writer(f)
    file.writerow(['Name', 'Age', 'Sex', 'Python_score','Education_level', 'Education', 'Faculty', "Years_experience", "image", "Text1", "Text2"])
      
    # generate applicant data from random combinations of variables
    for i in range(nr_applicants):                          
        file.writerow([
            names.get_full_name(), # name
            random.randint(18, 65), # age
            random.choice(sexes), # sex (OBS: make dependent on name;))
            random.randint(0, 100), # python score
            random.choice(edu_levels), # education level
            random.choice(education), # education level
            random.choice(faculties), # faculty
            random.randint(0, 50), # years experience (OBS: make dependent on age ;))
            random.choice(images),
            ''.join(random.choice(words) for i in range(10)), #random text 1 (CHANGE;))
            ''.join(random.choice(words) for i in range(20)) #random text 2 (CHANGE;))
            ])
