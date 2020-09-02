
class Person:
    def __init__(self, name, birthday, cpf, rg, address):
        self.name = name
        self.birthday = birthday
        self.cpf = cpf
        self.rg = rg 
        self.address = address
    print('Pessoa cadastrada com sucesso!')
# dailys é a quantidade de diárias
class Guest(Person):
    def __init__(self, name, birthday, cpf, rg, address, apt):
        super().__init__(name, birthday, cpf, rg, address)
        self.dailys = 0
        self.apt = apt


