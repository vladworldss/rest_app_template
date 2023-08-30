CREATE SCHEMA IF NOT EXISTS emails;

CREATE TABLE emails.email (
    id UUID NOT NULL PRIMARY KEY,
    smtp_address_from VARCHAR(128) NOT NULL,
    smtp_address_to VARCHAR(128) NOT NULL,
    subject VARCHAR(256) NOT NULL,
    body TEXT,
    send_date TIMESTAMP,
    status SMALLINT NOT NULL
)
