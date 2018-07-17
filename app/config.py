"""
This file contains all application Configurations
"""

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Define the application port and host 
APP_PORT = 2018
APP_HOST = '0.0.0.0'

# MYSQL Connection variables
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD= 'password'
MYSQL_DATABASE='nsrahwe'



