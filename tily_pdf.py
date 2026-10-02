import pypdf

with open("dummy.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    page = reader.get_page(0)
    page.rotate(90)
    writer = pypdf.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
