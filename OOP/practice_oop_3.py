class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):
        self.init_price = price
        new_price = self.init_price - self.init_price * self.__discount / 100
        return float(round(new_price, 2))

    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)