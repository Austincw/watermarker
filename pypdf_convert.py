# import pypdf

# template = pypdf.PdfReader(open("superduper.pdf", "rb"))
# watermark = pypdf.PdfReader(open("water.pdf", "rb"))
# output = pypdf.PdfWriter()

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)

# with open("watermaked_output.pdf", "wb") as outputFile:
#     output.write(outputFile)


# import pypdf
# import sys

# watermark = pypdf.PdfReader(sys.argv[1]).pages[0]
# writer = pypdf.PdfWriter(clone_from=f'{sys.argv[2]}')

# for page in writer.pages:
#     page.merge_page(watermark, over=False)

# writer.write('watermarked_output.pdf')
