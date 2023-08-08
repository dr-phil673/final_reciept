
import re

def buscar_cpf(texto):
    """Funcao para buscar CPF no texto que foi extraido.
    \nRetorna uma lista com os CPFs encontrados ou False se não existir.
    \nPara ser encontrado, o valor deve estar no formato xxx.xxx.xxx-xx.
    \nEx.:
    texto = texto extraido da imagem
    CPFs = buscar_cpf(texto)"""
    CPF = re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', texto)
    if len(CPF)>0:
        return CPF
    else:
        False


def buscar_data(texto):
    """Funcao para buscar datas no texto que foi extraido.
    \nRetorna uma lista com as datas encontradas ou False se não existir.
    \nPara ser encontrado, o valor deve estar no formato xx/xx/xxxx.
    \nEx.:
    texto = texto extraido da imagem
    Datas = buscar_data(texto)"""
    DATA = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
    if len(DATA)>0:
        return DATA
    else:
        False



def sumarizar_cpf(cpf):
    """Funcao para deixar o CPF em string.
    \nRetorna string.
    \nEx.:
    cpf = lista de CPFs encontrados no texto
    CPF = sumarizar_cpf(cpf)"""
    CPF = ""
    for i in cpf:
        CPF += i+". "
    return CPF


def sumarizar_datas(datas):
    """Funcao para deixar a Data em string.
    \nRetorna string.
    \nEx.:
    datas = lista de datas encontradas no texto
    DATAS = sumarizar_datas(datas)"""
    DATA = ""
    for i in datas:
        DATA += i+". "
    return DATA
