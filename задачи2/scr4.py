class Nikola:
    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"
        self.age = age
person1 = Nikola("Иван", 30)
print(person1.name)
print(person1.age)
person2 = Nikola("Николай", 20)
print(person2.name)
print(person2.age)