from database1 import connection
import datetime

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
            connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?", (self.balance, self.id))
            connection.execute("INSERT INTO transactions(account_id, transaction_time, amount) VALUES (?,?,?)",
                            (self.id, datetime.datetime.now(), amount))
            connection.commit()
            print(f"Na konto {self.name} zostało dodane {amount} PLN")
        return round(self.balance, 2)



    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self.balance:
            self.balance -= amount
            connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?", (self.balance, self.id))
            connection.execute("INSERT INTO transactions(account_id, transaction_time, amount) VALUES (?,?,?)",
                            (self.id, datetime.datetime.now(), -amount))
            connection.commit()
            print(f"Z konta {self.name} zostało wypłacone {amount} PLN.")
        return round(self.balance, 2)

    def send_founds(self, amount:float, account):
        self.withdraw(amount)
        account.deposit(amount)


if __name__ == '__main__':
    account = Account('Arek')
    account.deposit(100)
    account.deposit(0.2)
    balance = account.withdraw(6)
    print(balance)
