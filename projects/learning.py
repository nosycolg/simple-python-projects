import random
import os

os.system("clear")  ## ja limpa o chatzalha de otario

print("Hello World")  ## console.log()

name = "Cristhian"
lastName = "Felipe"

print(name + " " + lastName)  ## Cristhian Felipe

if 10 > 2:
    print("10 é maior que dois")
else:
    print("nunca que 2 é maior que 10")


def fullName():  ## function () => {}
    global full_name  ## isso aqui é doidera
    full_name = name + " " + lastName


fullName()  ## iniciando a function

print(full_name)

x = 1

print(x)
print(type(x))  ## <class 'int'>

n1 = 5
n2 = 2
x = complex(n1, n2)

print(x.real)
print(x.imag)

array = ["carro", 2, True]  ## array normal ne mas da pra substituir
tupla = ("carro", 2, True)  # tuplinha não da pra substituir
range = range(0, 100, 1)  # array
dict = {"nome": "Cristhian Felipe", "idade": 18}  ## basicamente um objetalhas

print(dict["idade"])

print(range)  ## da pra acreditar?? FOI DE 0 A 100 kkkkkkkkk

set = {2, 3, 4, 5, 4}  ## ele não repete

print(set)

frozenset = frozenset({2, 3, 4, 5, 4})  ## ele trava o set n entendi muito bem

print(frozenset)

num = 10

print(str(num))  ## virou string kk

string = "1"

print(int(string))  # virou number kkkkkkkk q otario

randomNumber = random.randrange(0, 60)  ## aleatorio

print(randomNumber)

randomArray = [
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60),
]  ## aleatorio mas em uma fucking array

print(randomArray)

language = "Python Py"

print(language[0:2])  ## Py

print(language[2:4])  ## th

print(len(language))  ## 6, é um length kkkkkkkkkkkkkkkkk mas pra string?

print(language.strip())  ## remove o espaço do começo, inutil

print(language.lower())  ## minusculo

print(language.upper())  ## maiusculo

print(language.replace("Python", "P"))  ## substitui

print(language.split(" ")[0])  ## vem só o python (como no js)

print("Python" in language)  ## true, verificou que tem um Python aí

dia = 3
mes = 7
ano = 2024

data = "{}/{}/{}"

print(data.format(dia, mes, ano))

empty = ""
lol = "lol"

print(bool(empty))  ## false
print(bool(lol))  ## true

cars = ["GOLF", "XJ6"]
cars.append("CIVIC")

print(cars)  ## ['GOLF', 'XJ6', 'CIVIC']

del cars[1]  ## DELETOU A XJ6 MANO

print(cars)  ## ['GOLF', 'CIVIC']

cars_copy = list(cars)  ## copiou na cara dura

cars.clear()  ## deletou tudo

print(cars)  ## []

print(cars_copy)  ## ['GOLF', 'CIVIC']

print(cars_copy + cars_copy)  ## ELE SIMPLESMENTE JUNTA AS LISTAS KKKK

for x in cars_copy:
    print(x)
    if x == "GOLF":
        print("É O GOLETA FEIO")
        break  ## tipo um throw

# input = input("Coloque seu nome: ")  ##inputzão o classico

# print(input) ## vai aparecer teu nome

i = 0

while i < len(cars_copy):
    print(cars_copy[i])
    i += 1
    if i == 5:
        break

cities = []

# city = input("COLOQUE UMA CIDADE: ")

# while city != "bahia":
#     cities.append(city)
#     city = input("COLOQUE UMA CIDADE: ")

print(cities)  ## vai imprimir as cidades

t_cars = ("SANDERO", "GOL")
l_cars = list(t_cars)
l_cars[1] = "XJ6"
l_cars.append("SANDERO RS")
t_cars = tuple(l_cars)
## uma forma de burlar a tupla ja q ela n pode ser alterada como um const.

print(t_cars)

array_cars = [["JUNIOR", "ANDRESSA"], ["CESAR", "ASTERIX"]]

print(array_cars[0][0])  ##junior como no js

car_details = {
    "Fabricante": "RENAULT",
    "Modelo": "SANDERO RS",
    "Cor": "BEGE",
    "Bólido?": "COM CERTEZA MENZINHO",
}

print(car_details.get("Cor"))  ## BEGE

print(car_details["Bólido?"])  ## COM CERTEZA MENZINHO


def texts(*t):  ## ELE ACEITA QUALQUER MERDA NO T
    for x in t:
        print(x)


texts("OLA", "TESTE")

soma = lambda a, b: a + b

print(soma(2, 5))


class Car:
    velMax: num
    ligado: bool
    cor = string

    def __init__(self, vel, on, color):
        self.velMax = vel
        self.ligado = on
        self.cor = color

    def console(self):
        print(self.cor)


sandero = Car(300, True, "Black")

sandero.console()  ## Black


class NPC:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def info(self):
        print(self.name)
        print(self.lastName)


NPC("Cristhian", "Felipe").info()


class Pessoa(NPC):
    def __init__(self, name, lastName):
        super().__init__(name, lastName)

    def info(self):
        super().info()


class Fodão(Pessoa):
    def __init__(self, name, lastName):
        super().__init__(name, lastName)

    def info(self):
        super().info()


npc = NPC("Cristiny", "Raquel")
pessoa = Pessoa("Cristiano", "Manoel")
fodão = Fodão("Patricia", "Simone")

npc.info()
pessoa.info()
fodão.info()

## muito foda heranças

try:
    print(UNDEFINED)
except:
    print("UNDEFINED não definido")
else:
    print("Tudo certo")
finally:
    print("nosycolg")

# number = -10

# if not type(number) is str:  ## not é o ! basicamente
#     raise Exception("Valor não permitido")
