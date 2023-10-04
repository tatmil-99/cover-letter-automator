import letter
import argparse
import applications


parser = argparse.ArgumentParser(prog='cover letter automator',
                                 description='Automate cover letters and store job related data')
subparser = parser.add_subparsers(
    title='subcommands', help='CRUD operations', dest='subparser_name')

# "create" sub-command
create_parser = subparser.add_parser(
    'create', help='create cover letter with arguments')
create_parser.add_argument('company', help='company name',)
create_parser.add_argument('position', help='job position',)

# parse args and call function based on command
args = parser.parse_args()
subcommand = args.subparser_name

if subcommand == 'create':
    company = args.company.lower()
    position = args.position.lower()
    letter.create(company, position)
