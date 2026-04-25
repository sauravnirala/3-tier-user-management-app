import os

if os.getenv("ENV") == "test":
    DATABASE_CONFIG = {
        "database": ":memory:"
    }
else:
    DATABASE_CONFIG = {
        "host": "db",
        "user": "root",
        "password": "root",
        "database": "testdb"
    }
