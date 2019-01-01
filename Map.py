'''La funcion Map aplica una funcion a a cada elemento de una lista iterable, devolviendo la lista de resultados'''


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


empleados = [
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "presidenta", 7500 ),
    Empleado("Antonio", "Administrativo", 2100),
    Empleado("Sara", "Secretaria", 2150 ),
    Empleado("Mario", "Botones", 1800),
]


def calculo_comision(empleado):
    empleado.salario = empleado.salario * 1.03
    return empleado


salarios = map(lambda emp: emp.salario, empleados)
salarios2 = [emp.salario for emp in empleados]
print("------SALARIO-------")
for salario in salarios2:
    print(salario)
print("-----SALARIO2--------")
for salario in salarios2:
    print(salario)


salarios_incrementados = map(lambda sal: sal * 1.03, salarios)




print("------EMPLEADOS-------")
for empleado in empleados:
    print(empleado)

empleados_salario_incrementado = map(calculo_comision, empleados)
print("-----EMPLEADOS SALARIO INCREMENTADO-----")
for empleado in empleados_salario_incrementado:
    print(empleado)