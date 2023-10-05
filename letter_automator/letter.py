from fpdf import FPDF


def create_pdf(letter):
    pdf = FPDF()
    pdf.set_margins(25.4, 25.4, 25.4)
    pdf.add_page()

    pdf.add_font("Arial", "", "/Users/tatienmiller/Library/Fonts/Arial.ttf", True)
    pdf.set_font("Arial")
    pdf.multi_cell(0, 5, letter)

    pdf.output("/Users/tatienmiller/Downloads/cover_letter.pdf")


def create(today, company, position):
    template = "template.txt"

    with open(template, "r") as letter:
        lines = letter.readlines()

    joined = "".join(lines)
    formatted = joined.format(today=today, company=company, position=position)

    create_pdf(formatted)
