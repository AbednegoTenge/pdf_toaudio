from pypdf import PdfReader
import pyttsx3


def extract_pdf(pdf):
    reader = PdfReader(pdf)
    text = ""
    for i in reader.pages:
        text += i.extract_text()
    return text.strip()

def read_pdf(pdf):
    engine = pyttsx3.init()
    engine.say(extract_pdf(pdf))
    engine.runAndWait( )


if __name__ == "__main__":
    read_pdf("example.pdf")