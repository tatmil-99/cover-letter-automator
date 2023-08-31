from datetime import datetime
from fpdf import FPDF


def format_pdf():
    pdf = FPDF()
    pdf.set_margins(25.4, 25.4, 25.4)
    pdf.add_page()
    pdf.add_font(
        'Arial', '', '/Users/tatienmiller/Library/Fonts/Arial.ttf', True)
    pdf.set_font('Arial')

    with open('letter.txt', 'r') as letter:
        lines = letter.readlines()

    for line in lines:
        pdf.multi_cell(0, 5, line)

    pdf.output('cover_letter.pdf')


def edit_letter(today, company, position):
    template = 'template.txt'
    file = 'letter.txt'

    with open(template, 'r') as letter:
        lines = letter.readlines()

    joined = ''.join(lines)
    formatted = joined.format(today=today, company=company, position=position)

    with open(file, 'w') as letter:
        letter.write(formatted)

    # format_pdf(letter)


current_datetime = datetime.now()
today = (
    f'{current_datetime.month}/'
    f'{current_datetime.day}/'
    f'{current_datetime.year}'
)
company = input('What company are you applying to? ')
position = input('What is the position? ')

edit_letter(today, company, position)
format_pdf()
