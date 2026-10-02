import pypdf
import sys

# increase recursion limit if using large pdf files
# sys.setrecursionlimit(sys.getrecursionlimit() * 5)
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)
