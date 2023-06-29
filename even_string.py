#!/usr/bin/python3

def myfunc(s):
    new_string = list(s)
    for item in range(len(new_string)):
        if item % 2 == 0:
            new_string[item] = str(new_string[item]).upper()
        else:
            new_string[item] = str(new_string[item]).lower()
    str_to_return = ''.join(new_string) 
#    for x in new_string:
#        str_to_return += x
    return str_to_return

teste = myfunc('Palmeiras')
print(teste)
