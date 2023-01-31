"""
Modulo para gerenciamento das pessoas cadastradas no programa de pos-graduacao.
"""

import pandas as pd
import re


def inicializa(fmt='csv'):
    '''
    Cria a tabela de pessoas com as colunas:
    - nome
    - CPF
    - passaporte
    - data_nascimento
    - nacionalidade
    - email_principal
    - email_secundario

    entrada(s)
    -------
    fmt : string
        String que define o formato da tabela a ser criada.
        As opcoes sao 'csv' ou 'excel'.
    '''

    if fmt not in ['csv', 'excel']:
        raise ValueError(
            "fmt deve ser 'csv' ou 'excel'"
        )

    # cria uma tabela vazia para cadastro de pessoas
    tabela = pd.DataFrame(
        {
            "nome": [],
            "CPF": [],
            "passaporte": [],
            "data_nascimento": [],
            "email_principal": [],
            "email_secundario": []
        }
    )

    if fmt == 'csv':
        tabela.to_csv('pessoas.csv')
    else: # fmt == 'excel'
        tabela.to_excel('pessoas.xlsx', index=False)


def adiciona(nome, CPF, passaporte, data_nascimento, nacionalidade, email_principal, email_secundario):
    '''
    Adiciona uma pessoa na tabela pessoas.

    entrada(s)
    ----------
    nome : string
        Nome da pessoa.
    CPF : int
        CPF da pessoa (somente numeros).
    passaporte : string
        Passaporte da pessoa.
    data_nascimento : string
        Data de nascimento no formato 'DD-MM-AAAA'.
    email_principal : string
        
    email_secundario : string

    '''

    # verifica se e-mail e valido
    #https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email) == None:
        aise ValueError(
            "endereco de em-mail invalido"
        )
