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


CREATE TABLE workers
(
    pesel      VARCHAR(11) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name  VARCHAR(255) NOT NULL,
    birthday   DATE         NOT NULL CHECK (birthday < GETDATE())
)

INSERT INTO workers (pesel, first_name, last_name, birthday)
VALUES ('1111111', 'Arek', 'Stoszek', '1993-11-21')