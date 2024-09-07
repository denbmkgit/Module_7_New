from pprint import pprint


name = 'products.txt'        # Назначели пепеменную для файла .txt
file_name = open(name, 'r')  # открыли и сказали что будем только читать
pprint(file_name.read())     # распечатали содержимое файла  - 'Product 1\nproduct 2' \n - перенос на новую строку
file_name.close()              # закрыли файл

file_for_append = open(name, 'a')
file_for_append.write('\nPotato , 50.5, Vegetables')
file_for_append.close()