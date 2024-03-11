import sys

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

valor_filtro=int(sys.argv[1])
filtro='mayor' if len(sys.argv) < 3 else sys.argv[2].lower()

if filtro not in ["menor","mayor"]:
    print("\nlo sentimos, no es una operacion valida...\n")
    exit()
elif filtro=="menor":
    menor_que=[k for k, v in precios.items() if valor_filtro > v]
    print(f"\nlos productos menores al umbral son {','.join(menor_que)}\n")
    
else:
    mayor_que=[k for k, v in precios.items() if valor_filtro < v]
    print(f"\nlos productos mayores al umbral son {','.join(mayor_que)}\n")
        