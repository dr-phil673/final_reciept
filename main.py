
import streamlit as st
from PIL import Image
import pytesseract
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR")
        self.texto = ""
        self.analisar_texto = False

    def main(self):
        st.title("OCR Programa")
        st.write("Optical Character Recognition (OCR) implementado com Python")
        imagem = st.file_uploader("Selecione alguma imagem", type=["png","jpg"])
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Texto extraído")
            self.texto = self.extract(img)
            st.write("{}".format(self.texto))
            
                

    
    def extract(self, img):
        texto = pytesseract.image_to_string(img, lang="eng")
        return texto

        
ocr = OCR()
ocr.main()
