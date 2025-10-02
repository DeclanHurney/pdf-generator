from fpdf import FPDF
# Example
#  style='B' (bold) - check more styles here: https://www.fpdf.org/en/doc/setfont.htm
#  w=0: cell extends to the width of the document. Anything greater than 0 means you can play around with width
#  border=0 means that the cell is not wrapped with a border
#  ln=1 (break line): next cell appears on next line. ln=0: next cell will be added after width of current cell
#  h=12 means the height of the cell, it is best to keep it same height as the font
#  txt='Hello there!' means the content of the cell
#  align="L" means the alignment of the text within the cell

pdf = FPDF(orientation='P', unit='mm', format='A4') # right click FPDF for lots more options

pdf.add_page()

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=25, h=12, txt='Hello there!', align="L", ln=0, border=1)
pdf.set_font(family='Arial', style='I', size=10)
pdf.cell(w=0, h=12, txt='I am on the same line because the ln attribute of the previous cell allowed me to be!',
         align="L", ln=1, border=1)
pdf.set_font(family='Times', style='U', size=8)
pdf.cell(w=0, h=12, txt='I am on the next line because the ln attribute of the previous cell allowed me to be!',
         align="L", ln=1, border=1)
pdf.set_font(family='Arial', style='I', size=12)
pdf.cell(w=180, h=12, txt='Next line because w attribute of this cell and ln attribute of the '
                        'previous cell allowed it!', align="L", ln=1, border=1)

# add another page manually
pdf.add_page()

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=25, h=12, txt='Hello there!', align="L", ln=0, border=1)
pdf.set_font(family='Arial', style='I', size=10)
pdf.cell(w=0, h=12, txt='I am on the same line because the ln attribute of the previous cell allowed me to be!',
         align="L", ln=1, border=1)
pdf.set_font(family='Times', style='U', size=8)
pdf.cell(w=0, h=12, txt='I am on the next line because the ln attribute of the previous cell allowed me to be!',
         align="L", ln=1, border=1)
pdf.set_font(family='Arial', style='I', size=12)
pdf.cell(w=180, h=12, txt='Next line because w attribute of this cell and ln attribute of the '
                        'previous cell allowed it!', align="L", ln=1, border=1)

# add more pages programmatically using pandas

pdf.output('Topics.pdf', 'F')


