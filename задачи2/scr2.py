class Soda:
    def __init__(self, additive=None):
        self.additive = additive
    
    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")
soda1 = Soda("клубничка")
soda2 = Soda()
soda1.show_my_drink()
soda2.show_my_drink()