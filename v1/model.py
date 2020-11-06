from datetime import date
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

        
    