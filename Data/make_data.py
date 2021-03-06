'''
This script randomly autogenerates a pool of job applications distinguished by a number of different factors.
'''
import random
import csv
import names
from os import listdir
from os.path import isfile, join
from motivation_letters import *
import numpy as np
import randomname

nr_applicants = 200 # set nr of applicants you want to generate

# set possible variable values (ADD MORE / CHECK THIS!)
sexes = ['female', 'male']
edu_levels = ["High School", "Bachelor", "Masters", "Ph.d.", "Postdoc"]
faculties = ['arts', 'sciences', 'engineering']
education = ['Information Sciences', 'Computer Scientist', 'Software Engineer', 'Media Science', 'Cognitive Science', 'Journalist']
workfields = ['databases', 'software programming', 'accounting', 'management', 'service industry']
words = ['this ', 'is ', 'a ', 'random ', 'selection ', 'of ', 'words ', 'yay ', 'banana ', 'cool ', 'hello ']
strength = ['Very commited and fierce', 'Love working with coworkers', 'Efficient and a teamplayer', 'Creative and solution-minded', 'Great with tech']
#Hobbies =['Hiking', 'football', 'Gaming', 'Skydiving']
skills =['communication', 'word', 'python', 'statistics', 'management', 'excel', 'java', 'analytics', 'powerpoint', 'problem solving', 'juristics']
images = [f for f in listdir('Data/Images') if isfile(join('Data/Images', f))]
personality_profiles = [f for f in listdir('Data/personality_plots') if isfile(join('Data/personality_plots', f))]
english_proficiency = ['No Proficiency', 'Limited', 'Professional', 'Advanced', 'Native']




# create a csv file named to contain the dataset
with open('Data/applicants' + str(nr_applicants) + '.csv', 'w', newline ='') as f: 
    file = csv.writer(f)
    file.writerow(['Name', 'Age', 'Sex', 'Python Score', 'Education Level', 'Education', 'Faculty', 'Workfields', "Years Experience", "image", "Personality Profiles", "Strength", "Text1", "Text2", "English Proficiency", "GPA", 'Skills', 'Motivation Letter', 'SQL Score', 'ID'])
    alias_list = []
      
    # generate applicant data from random combinations of variables
    for i in range(nr_applicants):
        skill = random.sample(skills, 3)
        alias = randomname.get_name(adj=('colors'), noun=('fruit'))
        alias = alias.replace('-', ' ')
        alias = alias.split(' ')[0].capitalize() + ' ' + alias.split(' ')[1].capitalize()
        while alias in alias_list:
            alias = randomname.get_name(adj=('colors'), noun=('fruit'))
            alias = alias.replace('-', ' ')
            alias = alias.split(' ')[0].capitalize() + ' ' + alias.split(' ')[1].capitalize()
        alias_list.append(alias)
        sex = random.choice(sexes)
        file.writerow([
            names.get_full_name(gender = sex), # name
            random.randint(18, 65), # age
            sex, # sex (OBS: make dependent on name;))
            random.randint(0, 100), # python score
            random.choice(edu_levels), # education level
            random.choice(education), # education
            random.choice(faculties), # faculty
            random.choice(workfields),
            random.randint(0, 25), # years experience (OBS: make dependent on age ;))
            random.choice(images),
            random.choice(personality_profiles),
            random.choice(strength),
            ''.join(random.choice(words) for i in range(10)), #random text 1 (CHANGE;))
            ''.join(random.choice(words) for i in range(20)), #random text 2 (CHANGE;))
            random.choice(english_proficiency), # English Proficiency
            random.uniform(0, 10), # GPA
            f'Skills: {skill[0]}, {skill[1]} and {skill[2]}',
            random.choice(motivation_letter),
            random.randint(0, 100), # python score
            alias,
            ])
