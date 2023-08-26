from datetime import datetime
import pickle

# current_datetime = datetime.now()
# today = (
#     f'{current_datetime.month}/'
#     f'{current_datetime.day}/'
#     f'{current_datetime.year}'
# )
# company = input('What company are you applying to? ')
# position = input('What is the position? ')

# cover_letter = f'''
# Tatien Miller
# Software Developer
# tatmil99@gmail.com

# {today}

# Dear Hiring Manager,

# My name is Tatien Miller and I am passionate about software development,
# computers, and just about anything tech related. I am looking for a role
# that will challenge me and allow me to grow as a natural problem solver.
# I enjoy troubleshooting and solving problems (traits that drew me to programming)
# and I feel my current skills would allow me to be successful in this role.
# I’m confident I would be a great fit as an employee for {company}
# and could responsibly fulfill the job duties and requirements of the
# {position} job vacancy.

# My education is somewhat diverse and includes knowledge from various institutes
# and areas of interest. Most recently, I am a graduate of DigitalCrafts,
# a leading educational institute that teaches software development. Before that,
# I earned college credits from Truman State University and
# Moberly Area Community College, where I studied business and economics.
# Since my graduation from DigitalCrafts, I have been working on personal projects.
# One of these projects being an e-commerce web app that sells coffee beans.
# This was a really fun, yet challenging, project that allowed me to practice
# important software development principles like state management.
# Since then, I have continued to further my education by completing certificates
# and studying computer science and information technology related material.
# In addition to continued learning, I have also been steady in coding various
# projects and improving my problem solving skills.

# The biggest take-away(s) from my educational experiences has been learning to
# never stop pursuing knowledge and learning how to think critically.
# I’ve had the opportunity to practice these skills through various projects
# (both individually and with a team) using software like Git and GitHub
# to collaborate. These are also skills that I've learned can persist outside
# of technical environments, and thus I apply them to everyday challenges.
# I believe these attributes make me a reliable candidate for the
# {position} role with {company}. I hope to hear back from you soon so we can
# learn more about each other and my fit for the role.
# Thank you for taking the time to consider me for this position.

# Best,
# Tatien Miller
# '''


def edit_letter(time, company, position):
    file = 'letter.txt'
    with open(file, 'r') as letter:
        for line in letter.readline():
            if 'time' in line:
                line.replace('time', time)
            elif 'company' in line:
                line.replace('company', company)


current_datetime = datetime.now()
today = (
    f'{current_datetime.month}/'
    f'{current_datetime.day}/'
    f'{current_datetime.year}'
)

company = input('What company are you applying to? ')
position = input('What is the position? ')

job_info_file = 'jobinfo.data'
job_info_list = []
try:
    read_file = open(job_info_file, 'rb')
    stored_info = pickle.load(read_file)
    print(stored_info)
    read_file.close()
except EOFError:
    job_info_list.append(
        {'Company': 'Temp Stop', 'Position': 'LAMP Developer'}
    )
    print(f'Initializing object: {job_info_list} as binary.')

    write_file = open(job_info_file, 'wb')
    pickle.dump(job_info_list, write_file)
    write_file.close()

    del job_info_list
