class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        commission = amount * 0.01
        self.balance += amount - commission
        print(f"Пополнение на {amount:.2f}. Комиссия: {commission:.2f}. Новый баланс: {self.balance:.2f}")

    def withdraw(self, amount):
        commission = amount * 0.01
        total = amount + commission
        if total > self.balance:
            print("Недостаточно средств для снятия.")
            return False
        self.balance -= total
        print(f"Снятие {amount:.2f}. Комиссия: {commission:.2f}. Новый баланс: {self.balance:.2f}")
        return True

    def check_balance(self):
        print(f"Баланс счета {self.account_number}: {self.balance:.2f}")
        return self.balance

if __name__ == "__main__":
    account1 = BankAccount("123", "Иван Ульянов", 1000.0)
    account2 = BankAccount("321", "Савелий Нафиков", 500.0)

    account1.check_balance()
    account2.check_balance()

    account1.deposit(500)
    account2.deposit(200)

    account1.withdraw(100)
    account2.withdraw(400)

    account1.check_balance()
    account2.check_balance()