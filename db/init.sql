CREATE SEQUENCE seq_account_no START 1;

CREATE TABLE IF NOT EXISTS nasabah (
    account_no VARCHAR(14) PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    nik VARCHAR(16) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    balance int NOT NULL DEFAULT 0
);

CREATE TYPE trx_code AS ENUM ('D', 'C');

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_no VARCHAR(14) NOT NULL,
    trx_code trx_code NOT NULL,
    amount int NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (account_no) REFERENCES nasabah (account_no)
);