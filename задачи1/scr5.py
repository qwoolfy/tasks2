import csv
def calculate_column_averages(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if not data:
            print("Файл пуст.")
            return
        columns = list(zip(*data))
        averages = []
        for col in columns:
            try:
                numbers = [float(num) for num in col]
                avg = sum(numbers) / len(numbers)
                averages.append(avg)
            except ValueError:
                print(f"Ошибка: {col}")
                return None
        return averages
filename = input("Введите имя файла: ")
averages = calculate_column_averages(filename)

if averages is not None:
    for i, avg in enumerate(averages, 1):
        print(f"Среднее столбца {i}: {avg:.2f}")