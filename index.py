import mysql.connector as mysql
import os
from datetime import datetime
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

# enter your server IP address/domain name
HOST = "HOST_IP / HOST_NAME" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "YOUR_DATABASE_NAME"
# this is the user you create
USER = "USER_NAME"
# user password
PASSWORD = "PASSWORD"

while True:
    now = datetime.now()
    dt_string = now.strftime("%H:%M")    
    print(dt_string)
    if config['Header']['Time'] == dt_string:        

        # Create a connection to the database
        try:
            connection = mysql.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE
            )
            if connection.is_connected():
                print("Connected to the database!")                                
                    
                # Build the mysqldump command for database backup
                backup_path = f'backup.sql'
                mysqldump_cmd = f'mysqldump -h {HOST} -u {USER} {DATABASE} > {backup_path}'
                os.system(mysqldump_cmd)

                print('Backup Complete')                
                
                time.sleep(100)
                
            connection.close()
            print("Connection closed.")

        except mysql.Error as err:
            print("Error:", err)

        time.sleep(30)


# Add this script in your startup folder in windows so that it runs every time the pc starts

# Make sure to add mysqldump_cmd in your environmental variables, path to mysqldump.exe will be provided against it

# ---------------------- #

# Make sure to add .my.cnf file in your root directiry with fowllowing text in it:

# [mysqldump]
# user=mysqluser
# password=secret

# ---------------------- #

# these commands must be executed on XAMP :

# CREATE USER 'root'@'%' IDENTIFIED BY 'some_pass';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

# FLUSH PRIVILEGES;