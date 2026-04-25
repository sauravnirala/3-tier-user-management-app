import os

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", "root"),
    "database": os.getenv("DB_NAME", "testdb")
    if os.getenv("ENV") == "test":
        DATABASE = "sqlite:///:memory:"
    else:
        DATABASE = "mysql"
}
