import io
from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

name = 'test.txt'
file_name = open(name, 'a', encoding='utf-8')
print(file_name.tell())
file_name.write(info[0] + '\n')
print(file_name.tell())
file_name.write(info[2] + '\n')
print(file_name.tell())

file_name = open(name, 'r')
print(file_name.read())


