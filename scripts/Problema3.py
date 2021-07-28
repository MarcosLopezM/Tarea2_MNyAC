# Problema 3

def suerte(n):
    if 10 <= n < 10 ** 6:
        nList = list(map(int, str(n)))
        if len(nList) % 2 == 0:
            Half = len(nList) // 2
            FirstHalf = nList[:Half]
            SecondHalf = nList[Half:]
            if sum(FirstHalf) == sum(SecondHalf):
                return True
            else:
                return False 
        else:
            print(f"El número tiene {len(nList)} dígitos.")
    else: 
        print("El número es muy grande.") 


"""
Utilizar funciones, en lugar de un bucle, es un poco más rápido.

Con [int(i) for i in str(n)]:
1.27 µs ± 81 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

Con list(map(int, str(n))):
1.04 µs ± 27.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""