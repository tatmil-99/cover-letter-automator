from datetime import datetime
from fpdf import FPDF
import argparse


def create_pdf(letter):
    pdf = FPDF()
    pdf.set_margins(25.4, 25.4, 25.4)
    pdf.add_page()

    pdf.add_font(
        'Arial', '', '/Users/tatienmiller/Library/Fonts/Arial.ttf', True)
    pdf.set_font('Arial')
    pdf.multi_cell(0, 5, letter)

    pdf.output('/Users/tatienmiller/Downloads/cover_letter.pdf')


def edit_letter(today, company, position):
    template = 'template.txt'

    with open(template, 'r') as letter:
        lines = letter.readlines()

    joined = ''.join(lines)
    formatted = joined.format(today=today, company=company, position=position)

    create_pdf(formatted)


class JobApplication:
    '''Represents jobs applied to'''

    applications = {}
    total = 0

    def __init__(self, company, position, date):
        self.company = company.lower()
        self.position = position.lower()
        self.date = date

        JobApplication.total += 1

    def update_company(self, company):
        old_company = self.company
        self.company = company.lower()
        new_company = self.company
        JobApplication.update_key(new_company, old_company)

    def update_position(self, position):
        self.position = position.lower()

    @classmethod
    def read_jobs(cls):
        print(f'Total applications: {cls.total}')
        for i in cls.applications:
            print((f'company: {cls.applications[i].company}, '
                   f'position: {cls.applications[i].position}, '
                   f'date: {cls.applications[i].date}'))

    # Need to list all applications to specific company (as tuple)?
    @classmethod
    def search_job(cls, job):
        if job in cls.applications:
            print(job)
        else:
            print('Not found')

    @classmethod
    def update_key(cls, new, old):
        cls.applications[new] = cls.applications.pop(old)
        print(cls.applications)

    @classmethod
    def store_job(cls, job):
        cls.applications[job.company] = job
        print(cls.applications)

    @classmethod
    def delete_job(cls, job):
        try:
            del cls.applications[job]
            print(f'Deleting job: {job}')
            JobApplication.total -= 1
        except KeyError:
            print(f'Could not find job: {job}.')


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

    edit_letter(today, company, position)

    job = JobApplication(company, position, today)
    JobApplication.store_job(job)
elif args.create:
    current_datetime = datetime.now()
    today = (f'{current_datetime.month}/'
             f'{current_datetime.day}/'
             f'{current_datetime.year}')
    company = input('What company are you applying to? ').strip()
    position = input('What is the position? ').strip()

    edit_letter(today, company, position)
