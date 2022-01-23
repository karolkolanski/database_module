from database_module import DatabaseConnector

db = DatabaseConnector()
db.add_new_agent(5, "Tomasz Agencki","2022-02-24 00:00:00")
print(db.select_all_agents())