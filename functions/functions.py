
import re


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
