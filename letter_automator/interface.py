import letter
import argparse
from jobs import Job
from datetime import datetime


parser = argparse.ArgumentParser(
    prog="cover letter automator",
    description="Automate cover letters and store job related data",
)
subparser = parser.add_subparsers(
    title="subcommands", help="CRUD operations", dest="subparser_name"
)

# "create" sub-command
create_parser = subparser.add_parser(
    "create", help="create cover letter with arguments"
)
create_parser.add_argument(
    "company",
    help="company name",
)
create_parser.add_argument(
    "position",
    help="job position",
)
create_parser.add_argument(
    "-s", "--store", action="store_true", help="store input data"
)

# "read" sub-command
read_parser = subparser.add_parser("read", help="search for companies applied to")
read_parser.add_argument("company", help="name of company applied to")

# args = parser.parse_args()
# subcommand = args.subparser_name

while True:
    cli_input = input('Enter command or "exit": ')
    if cli_input == "exit":
        break
    args = parser.parse_args(cli_input.split())
    subcommand = args.subparser_name

    # call function based on command entered
    if subcommand == "create":
        current_datetime = datetime.now()
        today = (
            f"{current_datetime.month}/"
            f"{current_datetime.day}/"
            f"{current_datetime.year}"
        )
        company = args.company.lower()
        position = args.position.lower()

        letter.create(today, company, position)

        if args.store:
            job = Job(company, position, today)
            Job.store(job)
    elif subcommand == "read":
        Job.search_job(args.company)
