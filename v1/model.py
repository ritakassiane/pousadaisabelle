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



