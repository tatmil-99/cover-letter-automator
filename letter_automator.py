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

    total_jobs = 0

    def __init__(self, company, position, date):
        self.company = company
        self.position = position
        self.date = date

    def company_name(self):
        print(f'{self.company}')

    def company_position(self):
        print(f'{self.position}')

    def date_applied(self):
        print(f'{self.date}')


current_datetime = datetime.now()
today = (f'{current_datetime.month}/'
         f'{current_datetime.day}/'
         f'{current_datetime.year}')
company = input('What company are you applying to? ').strip()
position = input('What is the position? ').strip()

edit_letter(today, company, position)

jobs = {}

job = Job(company, position, today)
jobs[company.lower()] = job
print(jobs)
