CREATE TABLE accounts
(
    account_id INT PRIMARY KEY IDENTITY,
    name       VARCHAR(255) NOT NULL,
    BALANCE    FLOAT        NOT NULL
)

CREATE TABLE transactions
(
    transaction_id   INT PRIMARY KEY IDENTITY,
    account_id       INT FOREIGN KEY REFERENCES accounts (account_id),
    transaction_time DATETIME,
    amount           FLOAT
)


