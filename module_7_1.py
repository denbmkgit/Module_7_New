from pprint import pprint

class Product:
    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self. weight = weight
        self.category = category

    def __str__(self):
        return str(self.name), float(self.weight), str(self.category)

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file_for_read = open(self.__file_name, 'r')


        return  (pprint(file_for_read.read()), print('it is get_products - file for read'),
                 file_for_read.close, print('it is get_products - close'), print('it is get_products = return'))


    def add(self, *products):
        for product in products:
            print(product)
            # if product not in self.get_products():
            #     file_for_append = open(self.__file_name, 'a')
            #     file_for_append.write(product)
            #     file_for_append.close()
            # else:
            #     print(f'{product} уже есть в магазине')

# sh = Shop()
# sh.get_products()
#pr = Product('beef', 10.0, 'meet')
# print(pr.__str__())
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

# s1.add(p1,p2,p3)

print(s1.get_products())