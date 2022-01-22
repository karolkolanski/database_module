from database_module import DatabaseConnector

db = DatabaseConnector()
print(db.select_number_of_agents())