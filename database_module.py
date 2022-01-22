import mysql.connector

class DatabaseConnector:
    def __init__(self, address="localhost", username="root", password="automaty", database_name="alk"):
        # Połączenie z bazą danych
        try:
            self.mydb = mysql.connector.connect(
                host = address,
                user = username,
                password = password,
                database = database_name
            )
            self.cursor = self.mydb.cursor()
            print("Connection extablished successfully")
        except:
            raise RuntimeError("Cannot connect to the database")
    def __del__(self):
        self.mydb.close()
        print("Connection closed")

db = DatabaseConnector()

