
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
            
            self.analisar_texto = st.sidebar.checkbox("Analisar texto")
            if self.analisar_texto==True:
                #cpf = fc.buscar_cpf(self.texto)
                datas = fc.buscar_data(self.texto)
                
                #if cpf==None:
                #    st.warning("Nenhum CPF encontrado.")
                #else:
                #    cpf = fc.sumarizar_cpf(cpf)
                #    st.success("CPF encontrado:")
                #    st.write(cpf)
        
                if datas==None:
                    st.warning("Nenhuma data encontrada.")
                else:
                    datas = fc.sumarizar_datas(datas)
                    st.success("Datas encontradas:")
                    st.write(datas)
                

    
    def extract(self, img):
        texto = pytesseract.image_to_string(img, lang="eng")
        return texto

        
ocr = OCR()
ocr.main()
