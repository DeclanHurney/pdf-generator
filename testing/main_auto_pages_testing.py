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
pdf.set_auto_page_break(auto=False, margin=0) #pages should not be broken automatically, this will permit us to
# configure headers and footers correctly and as we expect.

# add more pages programmatically using pandas
topics = pd.read_csv('../topics.csv')
# Block 2) if you want x number of pages for each topic, with each page containing the topic header, uncomment this
# code and comment out Block 3
# for index, topic in topics.iterrows():
#     for page in range(topic['Pages']):
#         pdf.add_page()
#         pdf.set_font(family='Times', size=24)
#         pdf.set_text_color(200, 200, 254)  #any or each of these values can range for 0 to 254, mixing red, green and blue
#         # for example pdf.set_text_color(254, 0, 0) means 254 red, 0 for green and 0 for blue, meaning all red
#         pdf.cell(w=0, h=12, txt=topic['Topic'], align="L", ln=1, border=0)
#
#     # next we set the coordinates of the line which will appear immediately under the txt=topic['Topic']
#     # these coordinates are x1, y1, x2 and y2. Their distances are measured in unit='mm'
#     # x1=from left margin, y1=from top margin, x2=from left margin, y2=from top margin. (Rem: PDF A4 is 210 mm
#     width 298mm height)
#     pdf.line(10, 21, 200, 21)

# here we are going to add a footer. To do this, note that total height of PDF is 298mm. x number of break lines have to
# be added from the top of page to reach the location for the footer. this can vary depending on whether a page
# already has a header or not. Bear in mind also that pdf.set_auto_page_break was set earlier
def set_footer(distance_from_top):
    pdf.ln(distance_from_top)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic['Topic'], align="R")


def set_header():
    pdf.set_font(family='Times', size=24)
    pdf.set_text_color(200, 200, 254)  # any or each of these values can range for 0 to 254, mixing red, green and blue
    # for example pdf.set_text_color(254, 0, 0) means 254 red, 0 for green and 0 for blue, meaning all red
    pdf.cell(w=0, h=12, txt=topic['Topic'], align="L", ln=1, border=0)
    # next we set the coordinates of the line which will appear immediately under the txt=topic['Topic']
    # these coordinates are x1, y1, x2 and y2. Their distances are measured in unit='mm'
    # x1=from left margin, y1=from top margin, x2=from left margin, y2=from top margin. (Rem: PDF A4 is 210 mm width)
    # pdf.line(10, 21, 200, 21)

def set_lines_in_main_body():
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)

# Block 3) if you want x number of pages for each topic, with only the first page containing the topic header,
# uncomment this code and comment out Block 2
for index, topic in topics.iterrows():
    footer_position = 261
    pdf.add_page()
    set_header()
    set_lines_in_main_body()
    set_footer(footer_position)

    for page in range(topic['Pages'] -1):
        footer_position = 270
        pdf.add_page()
        set_lines_in_main_body()
        set_footer(270)

pdf.output('Topics.pdf', 'F')


