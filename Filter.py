'''
Filter verifica que los elementos de una secuencia o lista cumplen
una condicion, devolviendo un iterador con los elementos que
cumplen dicha condicion.
Filter recibe una funcion como primer parametro que sera
la condicion a evaluar, seguido de una lista donde buscar'''

'''def numero_par(num):
    if num % 2 == 0:
        return True
'''

numeros = [17,24,7,39,8,51,92]

print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

empleados = [
    Empleado("Juan", "Director", 750000),
    Empleado("Ana", "presidenta", 850000 ),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 270000 ),
    Empleado("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda emp: emp.salario > 50000, empleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)