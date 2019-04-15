import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path, toPath):
    with open(path, "rb") as f:
        parser = PDFParser(f)
        pdfFile = PDFDocument()
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        pdfFile.initialize()
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        manager = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        interpreter = PDFPageInterpreter(manager, device)

        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, "a",encoding='utf-8') as f:
                        str = x.get_text()
                        #print(str)
                        f.write(str+"\n")

path = r"http.pdf"
toPath = r"pdf_read.txt"
readPDF(path, toPath)
