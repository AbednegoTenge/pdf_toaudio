from pypdf import PdfReader
import pyttsx3


reader = PdfReader('example.pdf')
page = reader.pages[0]
text = page.extract_text()

engine = pyttsx3.init()
engine.say(text)
engine.runAn
