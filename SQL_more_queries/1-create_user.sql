-- Creates the user user_0d_1 with all privileges.
-- Creates the user user_0d_1 with all privileges.

CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost'
   IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
