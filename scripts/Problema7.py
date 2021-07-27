# Problema 7

def characters(string):
    if 0 <= len(string) <= 100:
        if any(i.isalnum() for i in string):
            print(True)
        if any(i.isalpha() for i in string):
            print(True)
        if any(i.isdigit() for i in string):
            print(True)
        if any(i.isupper() for i in string):
            print(True)
        if any(i.islower() for i in string):
            print(True)
        # if not string:
        #     print("String vacía.")
        if string == "":
            print("String vacía.")
    else: 
        pass

# The any() function returns True if any element of an iterable is True. If not, any() returns False.

"""
El comando if not string puede causar confusiones, ya que muchas cosas evalúan a Falso (falsy) o Verdadero (truthy) en un contexto booleano.
Por ejemplo, 
In: bool("")
Out: False

In: bool("   ")
Out: False
"""