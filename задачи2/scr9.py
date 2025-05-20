class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Количество товара '{self.name}' увеличено на {amount}. Теперь: {self.quantity}")
        else:
            print("Ошибка: количество для увеличения должно быть положительным.")
    
    def decrease_quantity(self, amount):
        if amount > 0:
            if self.quantity >= amount:
                self.quantity -= amount
                print(f"Количество товара '{self.name}' уменьшено на {amount}. Теперь: {self.quantity}")
            else:
                print("Ошибка: нельзя уменьшить количество ниже нуля.")
        else:
            print("Ошибка: количество для уменьшения должно быть положительным.")
    
    def calculate_total_cost(self):
        total_cost = self.price * self.quantity
        print(f"Общая стоимость товара '{self.name}': {total_cost} руб.")
        return total_cost
    
    def __str__(self):
        return f"Продукт: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"

if __name__ == "__main__":
    product1 = Product("Яблоки", 50, 10)
    product2 = Product("Молоко", 80, 5)
    
    print(product1)
    print(product2)
    
    product1.increase_quantity(5)
    product2.increase_quantity(3)
    
    product1.decrease_quantity(3)
    product2.decrease_quantity(2)

    product1.decrease_quantity(20)
    
    total1 = product1.calculate_total_cost()
    total2 = product2.calculate_total_cost()
    
    print(f"Общая стоимость всех товаров: {total1 + total2} руб.")