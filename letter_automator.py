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


class JobApplication:
    '''Represents jobs applied to'''

    applications = {}

    def __init__(self, company, position, date):
        self.company = company.lower()
        self.position = position
        self.date = date

    def update_company(self, data):
        old_company = self.company
        self.company = data.lower()
        new_company = self.company
        JobApplication.update_key(new_company, old_company)

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


current_datetime = datetime.now()
today = (f'{current_datetime.month}/'
         f'{current_datetime.day}/'
         f'{current_datetime.year}')
company = input('What company are you applying to? ').strip()
position = input('What is the position? ').strip()

edit_letter(today, company, position)

job = JobApplication(company, position, today)
# job.store_job()
JobApplication.store_job(job)
job.update_company('New Google')
# JobApplication.search_job(job.company)
