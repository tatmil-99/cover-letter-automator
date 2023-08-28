from datetime import datetime


def edit_letter(today, company, position):
    template = 'template.txt'
    file = 'letter.txt'

    with open(template, 'r') as letter:
        lines = letter.readlines()

    joined = ''.join(lines)
    formatted = joined.format(today=today, company=company, position=position)

    with open(file, 'w') as letter:
        letter.write(formatted)


current_datetime = datetime.now()
today = (
    f'{current_datetime.month}/'
    f'{current_datetime.day}/'
    f'{current_datetime.year}'
)
company = input('What company are you applying to? ')
position = input('What is the position? ')

edit_letter(today, company, position)
