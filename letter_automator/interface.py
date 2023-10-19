import letter
import argparse
from jobs import Job
from datetime import datetime


# check if company in namespace is returned from parsed args
def get_company_arg(args):
    if 'company' in args:
        return args.company
    else:
        return


# check if position in namespace returned from parsed args
def get_position_arg(args):
    if 'position' in args:
        return args.position
    else:
        return


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
    "update", help="update name of company applied to")
update_parser.add_argument("-c", "--company", nargs=2,
                           help="name of company to update, followed by new company")
update_parser.add_argument("-p", "--position", nargs=2,
                           help="name of company to update, followed by new position")

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
        Job.get_job(company, print_obj=True)
    elif subcommand == "update":
        if company:
            job = Job.get_job(args.company[0])

            if job is not None:
                job.update_company(company[1])
        elif position:
            job = Job.get_job(args.position[0])

            if job is not None:
                job.update_position(position[1])
    elif args.quit:
        break
