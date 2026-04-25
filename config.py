import os

if os.getenv("ENV") == "test":
    DATABASE_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "test_db"
    }
else:
    DATABASE_CONFIG = {
        "host": "db",
        "user": "root",
        "password": "password",
        "database": "userdb"
    }
