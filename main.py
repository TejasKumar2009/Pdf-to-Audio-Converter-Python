import PyPDF3
import pyttsx3
import pdfplumber
from googletrans import Translator

translator = Translator()

filenameInput = input("Enter the pdf file name with .pdf : ")

file = f"ebooks/{filenameInput}"

book = open(file, "rb")
pdfRead= PyPDF3.PdfFileReader(book)
 
# Get no. of pages
pages = pdfRead.numPages

finalText = ""

from_language = 'en'

# Opening Pdf File
with pdfplumber.open(file) as pdf:
    # Reading Pdf page by page
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        text = text.replace("\n", " ")
        finalText += "\n" + text

# Getting audio file name as input
audiofileInput = input("Enter the generated audio file name with .mp3 : ")
audioFile = f"audiobooks/{audiofileInput}"
 
# Initializing pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

print('''\nAudiobook Languages : 
         1. English
         2. Hindi\n''')
language_input = int(input("Enter the langauge you want to make audio file : "))

if language_input==1:
    engine.setProperty("rate", 150)
    engine.save_to_file(finalText, audioFile)
    pass

elif language_input==2:
    engine.setProperty("rate", 160)
    finalText_hindi = translator.translate(finalText, 'hi', from_language)
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(finalText_hindi, audioFile)



engine.runAndWait()
print(f"Audio File Saved as '{audiofileInput}'")

