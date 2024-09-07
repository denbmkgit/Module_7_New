import io
from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, string):
    string_positions = {}
    number_str = 0
    file_for_open = open(file_name, 'a', encoding='utf-8')
    for str_ in string:
        bait_start_str = file_for_open.tell()
        file_for_open.write(str_ + '\n')
        number_str += 1
        string_positions[(number_str, bait_start_str)] = str_
    file_for_open.close()
    return string_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
