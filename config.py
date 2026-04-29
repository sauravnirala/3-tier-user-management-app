import os

if os.getenv("ENV") == "test":
    DATABASE_CONFIG = {
        "database": ":memory:"
    }
else:
    DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "testdb")
}
