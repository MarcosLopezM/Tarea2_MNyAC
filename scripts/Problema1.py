# Problema 1

def acomodo(tablas):
    Sorttablas = sorted(tablas)
    NSorttablas = list(range(Sorttablas[0], Sorttablas[-1] + 1))
    diff = len(NSorttablas) - len(Sorttablas)
    return diff