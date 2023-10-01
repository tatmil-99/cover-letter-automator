import letter
import argparse
from datetime import datetime
import applications

# Need to make CRUD commands with company, position, etc., arguments.
parser = argparse.ArgumentParser(prog='cover letter automator')

args = parser.parse_args()


# current_datetime = datetime.now()
# today = (f'{current_datetime.month}/'
#          f'{current_datetime.day}/'
#          f'{current_datetime.year}')
# company = input('What company are you applying to? ').strip()
# position = input('What is the position? ').strip()
