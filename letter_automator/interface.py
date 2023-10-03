import letter
import argparse
from datetime import datetime
import applications

parser = argparse.ArgumentParser(prog='cover letter automator',
                                 description='Automate cover letters and store job related data')
subparser = parser.add_subparsers(title='subcommands', help='CRUD operations')

create_parser = subparser.add_parser(
    'create', help='create cover letter with arguments')
create_parser.add_argument('company', help='company name')
create_parser.add_argument('position', help='job position')

args = parser.parse_args()


# current_datetime = datetime.now()
# today = (f'{current_datetime.month}/'
#          f'{current_datetime.day}/'
#          f'{current_datetime.year}')
# company = input('What company are you applying to? ').strip()
# position = input('What is the position? ').strip()
