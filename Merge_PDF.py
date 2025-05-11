from PyPDF2 import PdfMerger
pdfs = ["10th.pdf","8th.pdf" , "9th.pdf" ]
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()