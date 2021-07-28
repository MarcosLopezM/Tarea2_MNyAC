# Problema 1

def acomodo(tablas):
    if 1 <= len(tablas) <= 10:
        SortTablas = sorted(tablas)
        NSortTablas = list(range(SortTablas[0], SortTablas[-1] + 1))
        diff = len(NSortTablas) - len(SortTablas)
        return diff
    else:
            print("Lista inválida")

"""
La restricción acerca de la unidades máximas puede ser ignorada, ya que el número máximo que acepta Python es:

9223372036854775807.

Es decir, un número de 19 unidades.
"""