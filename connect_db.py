import os

from mysql import connector
from dotenv import load_dotenv


load_dotenv()
PASSWORD = "admin1234"

try:
    with connector.connect(
        host = "localhost",
        user = "root",
        password = PASSWORD
    ) as database:
        print(database)
except connector.Error as e:
    print(e)