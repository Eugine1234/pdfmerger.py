import PYPDF2
import sys
import os

merger = PYPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
        merger.write('CombinedDocAPA' 7 Student Paper.pdf):
        