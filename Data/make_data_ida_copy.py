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

# set possible variable values 
sexes = ['female', 'male']
edu_levels = ["High School", "Bachelor", "Masters", "Ph.d.", "Postdoc"]
faculties = ['Arts', 'Business', 'Science', 'Engineering']
education = ['Information Science', 'Law', 'Linguistics', 'Computer Science', 'Software Engineering', 'Media Science', 'Cognitive Science', 'Journalism']
workfields = ['Databases', 'Software programming', 'Advertising', 'Public relations', 'Natural Language Processing', 'SEO' , 'Accounting', 'Management', 'Copywriting']
strength = ['Very commited and fierce', 'Supportive of coworkers', 'Love working in a team', 'Efficient and goal-oriented', 'Creative and unconventional', 'A natural leader', 'Great with tech']
#Hobbies =['Hiking', 'football', 'Gaming', 'Skydiving']
skills =['Communication', 'Word', 'Python', 'MatLab', 'Statistics', 'Management', 'Excel', 'Java', 'Analytics', 'Powerpoint', 'Problem solving', 'Juristics']
images = [f for f in listdir('Data/Images') if isfile(join('Data/Images', f))]
personality_profiles = [f for f in listdir('Data/personality_plots') if isfile(join('Data/personality_plots', f))]
english_proficiency = ['No Proficiency', 'Limited', 'Professional', 'Advanced', 'Native']


# create a csv file named to contain the dataset
with open('Data/applicants' + str(nr_applicants) + '.csv', 'w', newline ='') as f: 
    file = csv.writer(f)
    file.writerow(['Name', 'Age', 'Sex', 'Python Score', 'Education Level', 'Education', 'Faculty', 'Workfields', "Years Experience", "image", "Personality Profiles", "Strength", "English Proficiency", "GPA", 'Skills', 'Motivation Letter', 'SQL Score', 'ID'])
      
    # generate applicant data from random combinations of variables
    for i in range(nr_applicants):
        skill = random.sample(skills, 3)
        alias = randomname.get_name(adj=('colors'), noun=('fruit'))
        alias = alias.replace('-', ' ')
        alias = alias.split(' ')[0].capitalize() + ' ' + alias.split(' ')[1].capitalize()
        sex = random.choice(sexes)
        age = random.randint(18, 65)
        if age >= 27:
            edu_level = random.choice(edu_levels) # old people
        else:
            edu_level = random.choice(["High School", "Bachelor", "Masters"]) # young people

        years_experience = random.randint(0, (age - 18))
        
        # write the file
        file.writerow([
            names.get_full_name(gender = sex), # name
            age, # age
            sex, # sex
            random.randint(0, 100), # python score
            edu_level, # education level
            random.choice(education), # education
            random.choice(faculties), # faculty
            random.choice(workfields),
            years_experience, # years experience
            random.choice(images),
            random.choice(personality_profiles),
            random.choice(strength),
            random.choice(english_proficiency), # English Proficiency
            random.uniform(0, 10), # GPA
            f'{skill[0]}, {skill[1]} & {skill[2]}',
            random.choice(motivation_letter),
            random.randint(0, 100), # SQL score
            alias
            ])
