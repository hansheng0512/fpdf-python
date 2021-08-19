from fpdf import FPDF
import subprocess
subprocess.call(["php", "tfpdf.php"], shell=True)
font_path = './font/unifont/'

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

# add font
pdf.add_font('Simsun', '', font_path + 'SIMSUN.ttf', uni=True)

pdf.set_margins(0, 0, 0)

pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!', 0, 1)

pdf.set_font('Times', '', 12)
pdf.cell(210, 10, 'Powered by FPDF.', 0, 0, 'C')

pdf.set_font('Arial', '', 12)
pdf.ln(50)
pdf.cell(85)
pdf.cell(0, 0, 'We have a new line.', 0)

# add image
pdf.image('cat_in_the_snow.jpg', 85, 32.5, 40)

# draw a line
pdf.line(85, 27.5, 125, 27.5)

# draw a rectangle
pdf.rect(80, 20, 50, 55)

# set fill, draw and font color
pdf.set_fill_color(128, 166, 197)
pdf.set_draw_color(41, 53, 50)
pdf.rect(80, 115, 50, 10, 'DF')

pdf.set_text_color(183, 208, 232)
pdf.ln(50)
pdf.cell(70)
pdf.cell(70, 0, 'We have a new line.', 0, 0, 'C')

# add popcat
for i in range(17):
    pdf.image('popcat.gif', 20 + i * 10, 102.5, 5)
    pdf.image('popcat.gif', 20 + i * 10, 82.5, 5)
    pdf.image('popcat2.jpg', 25 + i * 10, 102.5, 5)
    pdf.image('popcat2.jpg', 25 + i * 10, 82.5, 5)

# other languages text
pdf.set_text_color(0, 0, 0)
pdf.set_font('Simsun', '', 22)
pdf.ln(-24)
pdf.cell(90)
pdf.cell(0, 0, '欢迎光临', 0)

pdf.output('sample.pdf', 'F')
