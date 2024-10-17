class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, label, quantity):
        self.label = label
        self.quantity = quantity
    
    def get_info(self):
        return f'{self.label} (в наличии: {self.quantity})'


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, label, quantity, weight):
        super().__init__(label, quantity)
        self.weight = weight

    def get_weight(self):
        return f'{self.label} (в наличии: {self.quantity}). Вес: {self.weight} кг'


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, label, quantity, size):
        super().__init__(label, quantity)
        self.size = size
    
    def get_size(self):
        return f'{self.label} (в наличии: {self.quantity}). Размер: {self.size}'


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())