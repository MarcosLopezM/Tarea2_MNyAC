#Problema 6

def reemplazo(string):
    liststring = string.split()
    if 1 <= len(liststring) <= 10:
        newstring = "-".join(liststring)
        return newstring
    else:
        pass