from datetime import date
import requests
from xlsxwriter import Workbook
import pandas as pd 

lista_de_pessoas = []

class Person:
    def __init__(self, name, birthday, cpf, rg, address, email, number):
        self.name = name
        self.birthday = birthday
        self.cpf = cpf
        self.rg = rg 
        self.address = address
        self.email = email
        self.number = number
    print('Pessoa cadastrada com sucesso!')



    def age(self):
        today = date.today()
        year_birthday = int(self.birthday.split('-')[2])
        return today.year - year_birthday




# dailys é a quantidade de diárias
class Guest(Person):
    def __init__(self, name, birthday, cpf, rg, address, email, number):
        super().__init__(name, birthday, cpf, rg, address,email, number)
        daily = None
    
    


class Employee(Person):
    def __init__(self, name, birthday, cpf, rg, address, email, number):
        super().__init__(name, birthday, cpf, rg, address,email, number)
        admission_date = None



########----########

class Room:
    def __init__(self, id, idtype,double_bed, single_bed): # O id identifica o numero do quarto, idtype é o id que identifica o tipo de quarto
        self.id = id 
        self.idtype = idtype
        self.double_bed = double_bed
        self.single_bed = single_bed

class Room_Type:
    def __init__(self, id, name, description, daily_price):
        self.id = id
        self.name = name
        self.description = description
        self.daily_price = daily_price

class Booking:
    def __init__(self, id, previous_checkin, previous_checkout, id_roomtype, id_guest):
        self.id = id
        self.previous_checkin = previous_checkin
        self.previous_checkout = previous_checkout
        self.id_roomtype = id_roomtype
        self.id_guest = id_guest

class Accommodation:
    def __init__(self, id, checkin_date, checkout_date, checkin_time, checkout_time, room_id, guest_id):
        self.id = id 
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self. checkin_time = checkin_time 
        self. checkout_time = checkout_time 
        self.room_id = room_id
        self.guest_id = guest_id

class Payment: 
    def __init__(self, id, total_value, date, time, accommodation_id):
        self.id = id
        self.total_value = total_value
        self.date = date
        self.time = time
        self.accommodation_id = accommodation_id

class PaymentType:
    def __init__(self):
        self.options = ["Dinheiro", "Crédito", "Débito"]

class Consumption:
    def __init__(self, id, amount, idEmployee, idGuest, idItem):
        self.id = id
        self.amount = amount
        self.idEmployee = idEmployee
        self.idGuest = idGuest
        self.idItem = idItem
        
class ConsumptionItem: # The instance from this class is a consumption item
    def __init__(self, idItem, name_item, description, price):
        self.idItem = idItem
        self.name_item = name_item 
        self.description = description
        self.price = price 

### ADDRESS ##

class Address:
    def __init__(self, cep):
        self.cep = cep 
    
    def address_data(self):
        if len(self.cep) != 8:
            print("CEP Inválido")
            self.cep = input("Digite novamente:")
        r = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.cep))
        address = r.json()
        return address
## TESTANDO ##

# A função abaixo recebe um dicionario e retorna uma lista com todos os suas chaves. 
def return_keys(dict):
    lista = []
    for i in dict.keys():
        lista.append(i)
    return lista 

def anda_nas_pessoas():
    for i in lista_de_pessoas:
        print(i.__dict__)

def create_person(nome, niver, cpf, rg, email, cep, phone):
    pessoa = Person(nome, niver, cpf, rg, email, cep, phone)
    lista_de_pessoas.append(pessoa)
    return lista_de_pessoas

# A função a baixo recebe uma lista de objetos e retorna uma lista de dicionários com tais.

def obj_to_dict(list_object):
    list_of_dict = []
    for objecto in list_object:
        list_of_dict.append(objecto.__dict__)

    return list_of_dict




create_person('Rita','16-04-2000', '04211617524', '0548094', 'contaritakassiane@hotmail.com', '48760000', '75-99284099')
print(lista_de_pessoas)
lista_de_dicionario = obj_to_dict(lista_de_pessoas)
df = pd.DataFrame.from_dict(lista_de_dicionario)
print(df)

with pd.ExcelWriter('data-base-people.xlsx', mode='w') as writer:
    df.to_excel(writer, sheet_name='date')
    writer.save()





