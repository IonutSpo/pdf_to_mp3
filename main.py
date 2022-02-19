# pdf to text
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

# text to speech
from gtts import gTTS

# pygame for playing audio (MacOS things...)
import pygame


def pdf_to_text_to_audio(input_file):
    pdf_file = open(input_file, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr, TxtConverter)
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)

    txt_file = retData.getvalue()

    # print(txt_file)
    # with open(output, 'w') as of:
    #     of.write(txt_file)

    language = 'en'
    my_audio_document = gTTS(text=txt_file, lang=language, slow=False)
    my_audio_document.save("audio_document.mp3")

    pygame.mixer.music.load(my_audio_document)
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)



input_pdf = input("Where is your '.pdf' file located? \n")
pdf_to_text_to_audio(input_pdf)
