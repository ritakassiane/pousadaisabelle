import model 

init = """ 
 ##########################
#    SEJA BEM VINDO       #
 ##########################
"""
opcoes = """ 
    1. Cadastrar
    2. Sair
"""
def address_data(cep):
    if len(cep) != 8:
        print('CEP inválido!')
        cep = input('Digite novamente:')
    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    address = r.json()
    return address


def cadastro():7
    
    name = input('Nome:')
    birthday = input('Aniversário [dia-mes-ano]:')
    cpf = input("CPF: ")
    email = input("E-mail: ")
    cep = input("CEP: ")
    phone = input("Numero de telefone: ")
    person = model.Person(name, birthday, cpf, '', address_data(cep),email, phone)
    

