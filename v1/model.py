
class Person:
    def __init__(self, name, birthday, cpf, rg, address):
        self.name = name
        self.birthday = birthday
        self.cpf = cpf
        self.rg = rg 
        self.address = address

class Guest(Person):
    pass