
# 2023/11/15 00:00|Домашнее задание по теме "Режимы открытия файлов"



class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return  str_product




class Shop:
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        # pprint(prod_str)
        return prod_str

    def add(self, *products):
        file_get = self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

shop1 = Shop()
product1 = Product('Potato', 50.5,'Vegetables')
product2 = Product('Spaghetti', 3.4, 'Groceries')
product3 = Product('Potato', 5.5, 'Vegetables')
product4 = Product('Apple', 1.4, 'Fruits')



shop1.add(product1, product2, product3, product4, product2)
print(product2)
print(f'\n{shop1.get_product()}')