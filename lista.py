__author__='Agustin Albarran Delgado'

class Lista:

    def __init__(self):
        self.items = [10, 20]
        print('lista')
        print(self.items, '\n')
    def insertar(self):
        self.items.append(5)
        self.items.append(9)
        print('insertando numeros 5 y 9')
        print (self.items, '\n')
    def extend(self):
        self.items.extend([3, 6])
        print('utilizando extend numeros 3 y 6')
        print(self.items, '\n')
    def remove(self):
        self.items.remove(10)
        print('utilizando "remove" para el numero "10"')
        print(self.items, '\n')
    def indice(self):
        print('mostrando indice de numero 9')
        print(self.items)
        print('el indice del numero 9 es: ', self.items.index(9), '\n')
    def pop(self):
        self.items.pop()
        print('utilizando "pop" quita ultimo elemento de la lista')
        print(self.items, '\n')
    def contar(self):
        print('utilizando count para numero 20')
        print('el 20 aparece ', self.items.count(20), 'veces en la lista', '\n')
    def ordenar(self):
        print('utilizando metodo sort() para la lista')
        self.items.sort()
        print(self.items, '\n')
    def invertir(self):
        print('invirtiendo el orden de los numeros de la lista')
        self.items.reverse()
        print(self.items)