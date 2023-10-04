import letter
import argparse
from jobs import Job
from datetime import datetime


parser = argparse.ArgumentParser(prog='cover letter automator',
                                 description='Automate cover letters and store job related data')
subparser = parser.add_subparsers(
    title='subcommands', help='CRUD operations', dest='subparser_name')

# "create" sub-command
create_parser = subparser.add_parser(
    'create', help='create cover letter with arguments')
create_parser.add_argument('company', help='company name',)
create_parser.add_argument('position', help='job position',)
create_parser.add_argument(
    '-s', '--store', action='store_true', help='store input data')

# parse args and call function based on command
args = parser.parse_args()
subcommand = args.subparser_name

current_datetime = datetime.now()
today = (f'{current_datetime.month}/'
         f'{current_datetime.day}/'
         f'{current_datetime.year}')

if subcommand == 'create':
    company = args.company.lower()
    position = args.position.lower()
    letter.create(today, company, position)

    if args.store:
        job = Job(company, position, today)
        Job.store(job)
