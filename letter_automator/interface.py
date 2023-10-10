import letter
import argparse
from jobs import Job
from datetime import datetime


# check if company in namespace returned from parsed args
def get_company_arg(args):
    if 'company' in args:
        return args.company.lower()
    else:
        return None


# check if position in namespace returned from parsed args
def get_position_arg(args):
    if 'position' in args:
        return args.position.lower()
    else:
        return None


# create command-line parsers
parser = argparse.ArgumentParser(
    prog="cover letter automator",
    description="Automate cover letters and store job related data")
subparser = parser.add_subparsers(
    title="subcommands", help="CRUD operations", dest="subparser_name")

# "--quit" optional argument
parser.add_argument(
    "-q", "--quit", action="store_true", help="quit the interactive program")

# "create" sub-command
create_parser = subparser.add_parser(
    "create", help="create cover letter with arguments")

create_parser.add_argument("company", help="company name")
create_parser.add_argument("position", help="job position")
create_parser.add_argument(
    "-s", "--store", action="store_true", help="store input data")

# "read" sub-command
read_parser = subparser.add_parser(
    "read", help="search for companies applied to")
read_parser.add_argument("company", help="name of company applied to")

# "update" sub-command
update_parser = subparser.add_parser(
    "update", help="update name of company already applied to")

update_parser.add_argument(
    "-c", "--company", action="store_true", help="specify you want to update company info")
update_parser.add_argument("old_company", help="name of company to edit")
update_parser.add_argument("new_company", help="new name of company")


# interactive cli loop
print("Use '-q' to quit or '-h' for help")
while True:
    cli_input = input(">>> ")
    args = parser.parse_args(cli_input.split())
    subcommand = args.subparser_name

    company = get_company_arg(args)
    position = get_position_arg(args)
    current = datetime.now()
    today = f"{current.month}/{current.day}/{current.year}"

    if subcommand == "create":
        letter.create(today, company, position)

        if args.store:
            job = Job(company, position, today)
            Job.store(job)
    elif subcommand == "read":
        Job.search_job(company)
    elif subcommand == "update":
        pass
    elif args.quit:
        break
