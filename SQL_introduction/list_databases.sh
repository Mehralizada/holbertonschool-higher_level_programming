#!/bin/bash
# Script to list all databases on MySQL server

# MySQL connection parameters
MYSQL_HOST="localhost"
MYSQL_USER="root"
MYSQL_PASSWORD="your_mysql_password"

# SQL file containing the command to list databases
SQL_FILE="0-list_databases.sql"

# Execute MySQL command to list databases
echo "Listing databases..."
mysql -h"${MYSQL_HOST}" -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" < "${SQL_FILE}"

# End of script
echo "Script completed."
