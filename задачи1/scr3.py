import re
def pal(s):
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я]', '', s).lower()
    return cleaned == cleaned[::-1]
input_string = input("строка: ")
if pal(input_string):
    print("Это палиндром!")
else:
    print("Это не палиндром.")