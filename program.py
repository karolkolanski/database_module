from database_module import DatabaseConnector

db = DatabaseConnector()
print(db.select_all_agents_names())