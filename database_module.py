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

    def select_all_agents(self):
        self.cursor.execute("SELECT * from agenci;")
        result = self.cursor.fetchall()
        return result

    def select_number_of_agents(self):
        self.cursor.execute("select COUNT(*) from agenci;")
        result = self.cursor.fetchone()
        return result[0]

    def select_all_agents_names(self):
        self.cursor.execute("select agentname from agenci;")
        db_result = self.cursor.fetchall()
        result = []
        for r in db_result:
            result.append(r[0])
        return result

    # TODO
    def add_new_agent(self, id, name, licence_date):
        pass

    def __del__(self):
        self.mydb.close()
        print("Connection closed")

# Czy uruchomiłem program z tego pliku?
if __name__ == "__main__":
    db = DatabaseConnector()

