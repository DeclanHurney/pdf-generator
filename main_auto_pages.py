from fpdf import FPDF
import pandas as pd

# Example
#  style='B' (bold) - check more styles here: https://www.fpdf.org/en/doc/setfont.htm
#  w=0: cell extends to the width of the document. Anything greater than 0 means you can play around with width
#  border=0 means that the cell is not wrapped with a border
#  ln=1 (break line): next cell appears on next line. ln=0: next cell will be added after width of current cell
#  h=12 means the height of the cell, it is best to keep it same height as the font
#  txt='Hello there!' means the content of the cell
#  align="L" means the alignment of the text within the cell

pdf = FPDF(orientation='P', unit='mm', format='A4') # right click FPDF for lots more options


# add more pages programmatically using pandas
topics = pd.read_csv('topics.csv')
for index, topic in topics.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=24)
    pdf.set_text_color(200, 200, 254)  #any or each of these values can range for 0 to 254, mixing red, green and blue
    # for example pdf.set_text_color(254, 0, 0) means 254 red, 0 for green and 0 for blue, meaning all red
    pdf.cell(w=0, h=12, txt=topic['Topic'], align="L", ln=1, border=0)

    # next we set the coordinates of the line which will appear immediately under the txt=topic['Topic']
    # these coordinates are x1, y1, x2 and y2. Their distances are measured in unit='mm'
    # x1=from left margin, y1=from top margin, x2=from left margin, y2=from top margin. (Rem: PDF A4 is 210 mm width)
    pdf.line(10, 21, 200, 21)

pdf.output('Topics.pdf', 'F')


