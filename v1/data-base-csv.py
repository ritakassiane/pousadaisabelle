# This file put together all the functions that will be used for data manipulation.

import pandas as pd 
import requests

# The function recives a CEP and returns a dict with data about address
def address_data(cep):
    if len(cep) != 8:
        print('CEP inválido!')
        cep = input('Digite novamente:')
    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    address = r.json()
    return address

    


