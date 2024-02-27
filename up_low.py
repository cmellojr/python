#!/usr/bin/python3

def up_low(s):
    d = {'upper':0,'lower':0}

    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass

    print(f"Original string: {s}")
    print(f"Lowercase count: {d['lower']}")
    print(f"Uppercase count: {d['upper']}")

s = 'Olá, tudo bem? Só gostaria de dizer que o Palmeiras tem Mundial!'
up_low(s)
