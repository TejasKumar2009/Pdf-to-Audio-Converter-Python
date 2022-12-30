import PyPDF3
import pyttsx3
import pdfplumber

filenameInput = input("Enter the pdf file name with .pdf : ")

file = f"ebooks/{filenameInput}"

book = open(file, "rb")
pdfRead= PyPDF3.PdfFileReader(book)
 
# Get no. of pages
pages = pdfRead.numPages

finalText = ""

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
engine.setProperty("rate", 150)
engine.save_to_file(finalText, audioFile)
engine.runAndWait()
print(f"Audio File Saved as '{audiofileInput}'")

