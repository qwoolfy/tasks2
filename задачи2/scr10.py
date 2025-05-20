class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject_name, grade):
        self.subjects[subject_name] = grade
        print(f"Предмет '{subject_name}' с оценкой {grade} добавлен для студента {self.name}.")

    def remove_subject(self, subject_name):
        if subject_name in self.subjects:
            del self.subjects[subject_name]
            print(f"Предмет '{subject_name}' удалён для студента {self.name}.")
        else:
            print(f"Предмет '{subject_name}' не найден в списке студента {self.name}.")

    def calculate_average_grade(self):
        if not self.subjects:
            print(f"У студента {self.name} нет предметов для расчёта среднего балла.")
            return 0
        average = sum(self.subjects.values()) / len(self.subjects)
        print(f"Средний балл студента {self.name}: {average:.2f}")
        return average

if __name__ == "__main__":
    student1 = Student("Ульянов Иван", 20)
    student2 = Student("Нафиков Савелий", 21)

    student1.add_subject("Математика", 5)
    student1.add_subject("Физика", 5)
    student1.add_subject("Обществознание", 4)
    student1.add_subject("История", 3)

    student2.add_subject("Литература", 4)
    student2.add_subject("История", 3)
    student2.add_subject("Физика", 5)

    student1.remove_subject("Физика")
    student1.remove_subject("Химия")

    student1.calculate_average_grade()
    student2.calculate_average_grade()