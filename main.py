import re
import streamlit as st
from PIL import Image
import pytesseract
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Reciept OCR")
        self.text = ""

    def main(self):
        st.title("Reciept OCR")
        st.write("Optical Character Recognition (OCR) implemented with Python")
        image = st.file_uploader("Select an image.", type=["png","jpg"])
        if image:
            img = Image.open(image)
            st.image(img, width=350)
            st.info("Extracted Text")
            self.text = self.extract(img)
            st.write("{}".format(self.text))
            try:
                trash, x = str(self.text).split("Tax")
                print(re.findall(r"(\d+)M", x))
            except ValueError:
                try:
                    trash, x = str(self.text).split("TAX")
                    print(re.findall(r"(\d+)M", x))
                except:
                    pass
            
                

    
    def extract(self, img):
        text = pytesseract.image_to_string(img, lang="eng")
        return text
ocr = OCR()
ocr.main()
