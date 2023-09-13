from datetime import datetime
from fpdf import FPDF


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


class Job:
    '''Represents jobs applied to'''

    jobs = {}

    def __init__(self, company, position, date):
        self.company = company.lower()
        self.position = position
        self.date = date

    def store_job(self):
        Job.jobs[self.company] = self
        print(Job.jobs)

    def update_key(self, new, old):
        Job.jobs[new] = Job.jobs.pop(old)
        print(Job.jobs)

    def update_company(self, data):
        old_company = self.company
        self.company = data.lower()
        new_company = self.company
        self.update_key(new_company, old_company)

    @classmethod
    def search_job(cls, job):
        if job in cls.jobs:
            print(job)
        else:
            print('Not found')


current_datetime = datetime.now()
today = (f'{current_datetime.month}/'
         f'{current_datetime.day}/'
         f'{current_datetime.year}')
company = input('What company are you applying to? ').strip()
position = input('What is the position? ').strip()

edit_letter(today, company, position)

job = Job(company, position, today)
job.store_job()
job.update_company('New Google')
# Job.search_job(job.company)
