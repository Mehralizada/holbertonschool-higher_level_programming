CREATE DATABASE IF NOT EXISTS hbtn_test_db_7;
USE hbtn_test_db_7;

CREATE TABLE IF NOT EXISTS your_table_name (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO your_table_name (id, name) VALUES (89, 'Holberton School');
