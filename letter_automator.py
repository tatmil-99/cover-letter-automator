from datetime import datetime

current_datetime = datetime.now()
today = (
    f'{current_datetime.month}/'
    f'{current_datetime.day}/'
    f'{current_datetime.year}'
)

company = input('What company are you applying to? ')
