import pypdf
import sys

pdf = sys.argv[1]
wtrmrk_file = sys.argv[2]


def add_watermark(pdf_file, wtrmrk):
    watermark = pypdf.PdfReader(wtrmrk).pages[0]
    writer = pypdf.PdfWriter(clone_from=pdf_file)
    for page in writer.pages:
        page.merge_page(watermark, over=False)
    writer.write("superwatermark.pdf")


add_watermark(pdf, wtrmrk_file)
