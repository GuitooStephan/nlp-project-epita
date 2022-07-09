import sys
import PyPDF2
import re
import spacy


def load_spacy_model():
    nlp = spacy.load('./data/models/ner')
    return nlp


def pdf_to_txt(file):
    fileReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    countpage = fileReader.getNumPages()
    count = 0
    texts = []
    for count in range(countpage):
        pageObj = fileReader.getPage(count)
        text = pageObj.extractText()
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = re.sub("\s+ | [・.]", ' ', text)
        text = re.sub("[^a-zA-Z0-9,.:] ", ' ', text)
        texts.append(text)
    return '\n'.join(texts)


# Get arrgs from command line
args = sys.argv
file_path = args[1]

# Get content of pdf file
pdf_content = pdf_to_txt(file_path)


# Load spacy model
nlp = load_spacy_model()
doc = nlp(pdf_content)

# Print result
print(f'''The following entities were found in the PDF file:''')
for ent in doc.ents:
    print(f'Text: {ent.text}, Label: {ent.label_}')
print('''\n''')
