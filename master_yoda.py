#!/usr/bin/python3

# using the list reverse() method 

def master_yoda(text):
    text_list = list(text.split(' '))
    text_list.reverse()
    print(text_list)
    str_to_return = ' '.join(text_list)
    return str_to_return

#using string slicing 
def master_yoda_slice(text):
    return ' '.join(text.split(' ')[::-1])

x = master_yoda('I am your father')
print(x)
y = master_yoda_slice('You are from the dark side')
print(y)
