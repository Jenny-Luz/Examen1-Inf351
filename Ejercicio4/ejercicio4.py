# -*- coding: utf-8 -*-
"""Ejercicio4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ktaoeEFQNo2GkiIyDcJdZhaNfYcA_I2_
"""

# EJERCICIO 4
class Persona:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        self.padres = []
        self.hijos = []

    def agregar_padre(self, padre):
        self.padres.append(padre)

    def agregar_madre(self, madre):
        self.padres.append(madre)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return f'{self.nombre} ({self.genero})'


# Definir personas
abuelo_pat = Persona("Juan", "M")
abuela_pat = Persona("Lucia", "F")
abuelo_mat = Persona("Paulino", "M")
abuela_mat = Persona("Maria", "F")

padre = Persona("Adrian", "M")
madre = Persona("Guadalupe", "F")

hijo1 = Persona("Grover", "M")
hijo2 = Persona("Veronica", "F")
hijo3 = Persona("Rogers", "M")
hijo4 = Persona("Jenny", "F")
hijo5 = Persona("Adriana", "F")

# Establecer relaciones
padre.agregar_padre(abuelo_pat)
padre.agregar_madre(abuela_pat)
madre.agregar_padre(abuelo_mat)
madre.agregar_madre(abuela_mat)

padre.agregar_hijo(hijo1)
padre.agregar_hijo(hijo2)
padre.agregar_hijo(hijo3)
padre.agregar_hijo(hijo4)
padre.agregar_hijo(hijo5)

madre.agregar_hijo(hijo1)
madre.agregar_hijo(hijo2)
madre.agregar_hijo(hijo3)
madre.agregar_hijo(hijo4)
madre.agregar_hijo(hijo5)

# Mostrar relaciones
print(f"Padre: {padre}")
print(f"Madre: {madre}")
print(f"Hijos del padre: {padre.hijos}")
print(f"Hijos de la madre: {madre.hijos}")
print(f"Abuelos paternos del padre: {padre.padres}")
print(f"Abuelos maternos de la madre: {madre.padres}")