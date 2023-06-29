#!/usr/bin/python3

string = str(input('Escreva uma frase: ')).strip()
print('A string tem {} caracteres, onde {} são letras e {} são espaços.'.format(len(string),len(string) - string.count(' '),string.count(' ')))
print('A string em maiúsculas é: {}'.format(string.upper()))


# testing the old string format 
print('A string contém %d letras S' % int(string.count('S')))
name = 'Carlos'
print('Hello %s' % name)

def print_name(name):
  '''
  Função que imprime um nome
  '''
  print("Hello " +name)

print_name("Jose")
