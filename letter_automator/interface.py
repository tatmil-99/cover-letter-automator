import letter
import argparse
from jobs import Job
from datetime import datetime


def update_job(attr, parser_arg):
    old_job = parser_arg[0].lower()
    new_job = parser_arg[1].lower()
    job = Job.get_job(old_job)

    if job:
        # uses setattr() to make updates more dynamic
        setattr(job, attr, new_job)


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

create_parser.add_argument(
    "-c", "--company", help="company name", nargs='+', required=True)
create_parser.add_argument(
    "-p", "--position", help="job position", nargs='+', required=True)
create_parser.add_argument(
    "-s", "--store", action="store_true", help="store input data")

# "read" sub-command
read_parser = subparser.add_parser(
    "read", help="search for companies applied to")
read_parser.add_argument(
    "company", help="name of company applied to", nargs='+')

# "update" sub-command
update_parser = subparser.add_parser(
    "update", help="update name of company applied to")
update_parser.add_argument("-c", "--company", nargs=2,
                           help="name of company to update, followed by new company")
update_parser.add_argument("-p", "--position", nargs=2,
                           help="name of company to update, followed by new position")

# "delete" sub-command
delete_parser = subparser.add_parser(
    "delete", help="delete company applied to")
delete_parser.add_argument("company", help="name of company applied to")
delete_parser.add_argument("position", help="name of position applied to")

# interactive cli loop
print("Use '-q' to quit or '-h' for help")

while True:
    cli_input = input(">>> ")
    args = parser.parse_args(cli_input.split())
    subcommand = args.subparser_name

    current = datetime.now()
    today = f"{current.month}/{current.day}/{current.year}"
    joined_company = None
    joined_position = None
    # assigns value (if not None) in enclosing scope to make code DRY
    if "company" in args:
        joined_company = " ".join(args.company)
    if "position" in args:
        joined_position = " ".join(args.position)

    if args.quit:
        break

    match subcommand:
        case "create":
            letter.create(today, joined_company, joined_position)

            if args.store:
                job = Job(joined_company, joined_position, today)
                Job.store(job)
        case "read":
            Job.get_job(joined_company, print_obj=True)
        case "update":
            if args.company:
                update_job("company", args.company)
            elif args.position:
                update_job("position", args.position)
        case "delete":
            application_num = Job.get_job(args.company, position=args.position)

            if application_num:
                Job.delete(application_num)
