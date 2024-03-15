# funcion que calcula factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# funcion que calcula la productoria
def productoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado


def calcular(**kwargs):
    for clave, valor in kwargs.items():
        # Revisa si 'fact' está en la clave para calcular el factorial.
        if "fact" in clave:
            print(f"El factorial de {valor} es {factorial(valor)}")
        # Revisa si 'prod' está en la clave para calcular la productoria.
        elif "prod" in clave:
            print(f"La productoria de {valor} es {productoria(valor)}")


#ejemplo del calculo
calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)
