"""
All of settings information of this Rest API project will hold here
Created at: 28-07-2018
"""
__author__ = " Vubon Roy"

# Database settings

DATABASE = {
    "dbname": "hellofresh",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# end Database settings

INSTALL_APPS = [
    'recipes',
]