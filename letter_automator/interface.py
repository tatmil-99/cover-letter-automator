import letter
import argparse
from datetime import datetime
import applications

# Need to make CRUD commands with company, position, etc., arguments.
parser = argparse.ArgumentParser()
parser.add_argument(
    '--create', help='create pdf for cover letter', action='store_true')
parser.add_argument(
    '--store', help='store job data', action='store_true')
parser.add_argument(
    '--list jobs', help='list all jobs applied to', action='store_true')
parser.add_argument(
    '--search', help='seaches if company exists in applications',
    action='store_true')
args = parser.parse_args()

# Using optional arguments here instead of positional because the data
# needed requires custom input from the user
if args.create and args.store:
    current_datetime = datetime.now()
    today = (f'{current_datetime.month}/'
             f'{current_datetime.day}/'
             f'{current_datetime.year}')
    company = input('What company are you applying to? ').strip()
    position = input('What is the position? ').strip()

    letter.edit(today, company, position)

    job = applications.job(company, position, today)
    applications.job.store(job)
elif args.create:
    current_datetime = datetime.now()
    today = (f'{current_datetime.month}/'
             f'{current_datetime.day}/'
             f'{current_datetime.year}')
    company = input('What company are you applying to? ').strip()
    position = input('What is the position? ').strip()

    letter.edit(today, company, position)
