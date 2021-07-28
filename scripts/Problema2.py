# Problema 2

def characters(string1, string2):
    if 1 <= len(string1) <= 15 and 1 <= len(string2) <= 15:
        asciiletters = set("abcdefghijklmnopqrstuvwxyz")
        if all((i in asciiletters) for i in string1) and  all((i in asciiletters) for i in string2):
            String1List = list(string1)
            String2List = list(string2)
            c = 0
            for j in String1List:
                if j in String2List:
                    c += 1
                    String2List.remove(j)
            return c 

        else:
            print("String inválida.")
    else:
        print("Número de caracteres inválidos.")

# The all() function returns True if all elements in the given iterable are true. If not, it returns False.