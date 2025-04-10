from database1 import connection


class Account:

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self.balance = opening_balance

        connection.execute("INSERT INTO accounts(name,balance) VALUES (?,?)",
                           (self.name, self.balance))

        cursor = connection.execute("SELECT @@IDENTITY AS ID")

        self.id = cursor.fetchone()[0]

        connection.commit()

        print(f'Konto zostało utworzone dla {self.name} z balansem {self.balance}')

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            print(f"Na konto {self.name} zostało dodane {amount} PLN")
        return round(self.balance, 2)

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Z konta {self.name} zostało wypłacone {amouunt} PLN.")
        return round(self.balance, 2)


if __name__ == '__main__':
    account = Account('Arek')
    account.deposit(10)
    account.deposit(0.1)
    balance = account.withdraw(5)
    print(balance)
