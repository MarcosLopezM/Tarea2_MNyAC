# Problema 1

def acomodo(tablas):
    if 1 <= len(tablas) <= 10:
        Sorttablas = sorted(tablas)
        NSorttablas = list(range(Sorttablas[0], Sorttablas[-1] + 1))
        diff = len(NSorttablas) - len(Sorttablas)
        return diff
    else:
            print("Lista inválida")


"""
La restricción acerca de la unidades máximas puede ser ignorada, ya que el número máximo que acepta Python es:

9223372036854775807.

Es decir, un número de 10^19.
"""