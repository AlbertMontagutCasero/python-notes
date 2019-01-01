'''
Las funciones lambdas son funciones que no tienen nombre.
Se escriben utilizando la palabra clave reservada lambda
seguido de un listado de argumentos o parametros
seguido de dos puntos (simbolizando la palabra reservada return)
y la implementacion de dicha funcion que retornara
'''

'''
Codigo de ejemplo normal
'''
'''
def area_triangulo(base , altura):
    return(base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)

print(triangulo1)
print(triangulo2)
'''


'''
Codigo de ejemplo utilizando funciones lambda
'''

'''
area_triangulo = lambda base, altura: (base*altura)/2

print(area_triangulo(3,5))
'''


destacar_valor = lambda comision:"¡{}! €".format(comision)

comision_ana = 15585

print(destacar_valor(comision_ana))
