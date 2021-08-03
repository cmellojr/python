string = str(input('Escreva uma frase: ')).strip()
print('A string tem {} caracteres, onde {} são letras e {} são espaços.'.format(len(string),len(string) - string.count(' '),string.count(' ')))
print('A string em maiúsculas é: {}'.format(string.upper()))
