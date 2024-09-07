file = open('file1.txt', 'r', encoding='utf-8')

# print(file.read())
list_1 = []

# str_ = file.read()
# print(str_)
#
# a, b = file.read().split()
# list_1.append(a)
# list_1.append(b)

for i in file.read().split():
    print(i)
    list_1.append(i)
print(list_1)