def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
a = int(input("начало интервала: "))
b = int(input("конец интервала: "))
prime_sum = 0
for num in range(a, b + 1):
    if is_prime(num):
        prime_sum += num
print(f"Сумма чисел в интервале: {prime_sum}")