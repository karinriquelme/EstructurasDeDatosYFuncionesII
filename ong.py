import math

def factorial(numero):
    return math.factorial(numero)


def productoria(lista):
    return math.prod(lista)
    

def calcular(**kwargs):
    for k,v in kwargs.items():
        if k[:4]=="fact":
            print(f"el factorial del numero {v} es {factorial(v)}")
            
        elif k[:4]=="prod":
            print(f"la productoria del numero {v} es {productoria(v)}")
        else:
            print("no se reconoce la operacion solicitada")
    exit()    
        
print(calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6, prod_2=[3,6,4,2,8]))
