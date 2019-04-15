
import docx

file=docx.Document("论语.doc")

for para in file.paragraphs:
    print(para.text)

