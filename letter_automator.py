from datetime import datetime
import pickle


def edit_letter(company, position, previous_jobs):
    previous_company = previous_jobs[-1]['Company']
    previous_position = previous_jobs[-1]['Position']

    file = 'letter.txt'
    content_changes = []

    with open(file, 'r') as letter:
        for line in letter.readlines():
            if previous_company in line:
                change = line.replace(previous_company, company)
                content_changes.append(f'{change}')
            elif previous_position in line:
                change = line.replace(previous_position, position)
                content_changes.append(f'{change}')
            else:
                content_changes.append(f'{line}')

    with open(file, 'w') as letter:
        letter.writelines(content_changes)


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
    with open(job_info_file, 'rb') as read_file:
        stored_info = pickle.load(read_file)

    edit_letter(company, position, stored_info)

    stored_info.append({'Company': company, 'Position': position})
    print(stored_info)

    with open(job_info_file, 'wb') as write_file:
        pickle.dump(stored_info, write_file)
except EOFError:
    job_info_list.append(
        {'Company': 'Temp Stop', 'Position': 'LAMP Developer'}
    )
    print(f'Initializing object: {job_info_list} as binary.')

    with open(job_info_file, 'wb') as write_file:
        pickle.dump(job_info_list, write_file)

    del job_info_list
