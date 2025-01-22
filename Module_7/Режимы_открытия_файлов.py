class Product:

    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        file = open(self.__file_name, 'r')
        file_text = file.read()
        file.close()
        return file_text

    def add(self, *products) -> None:
        current_products_raw: list[str] = self.get_products().split('\n')
        current_products: list[str] = []
        for product in current_products_raw:
            name = product.split(',')[0]
            current_products.append(name.casefold())
        products_to_add: list[str] = []
        for product in products:
            if product.name.casefold() in current_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                # current_products_raw.append(str(product))
                products_to_add.append(str(product) + '\n')
        file = open(self.__file_name, 'a')
        file.write(''.join(products_to_add))
        file.close()

def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2) # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
                

if __name__ == "__main__":
    main()

         

        
        
