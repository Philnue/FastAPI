import sqlite3
from sqlite3 import Error

class BusinesssLogic():
    
    def __init__(self):
        try:
            self.con = sqlite3.connect("../personenliste.db")
            self.cur = self.con.cursor()
            print("connected")
        except Exception as e:
            print("Error connecting: " + str(e.args))

    def get_item_by_id(self, id):
        try:
            command = "SELECT * FROM Personen where id == ?"
            self.execute_command_tuple(command, (id,))
            p = self.cur.fetchone()
            return p
        except Exception as e:
            print("Error getting item by id" + str(e))

    def get_all_entries(self):

        try:
            command = "SELECT * FROM Personen"
            self.execute_command(command)
            s = []
            for item in self.cur.fetchall():
                d = {"id": item[0], "vorname" : item[1], "nachname" : item[2]}
                s.append(d)
            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

    def insert_into(self, vorname, nachname):

        try:
            command = "INSERT INTO Personen (Vorname, Nachname) VALUES (?,?)"
            self.execute_command_tuple(command, (vorname,nachname))
            self.commit_changes()
            return f"Added Person: {vorname} {nachname}"
        except Exception as e:
            return( "Adding person error" + str(e.args))

    def delete_by_id(self, id):
        try:
            command = "DELETE FROM Personen WHERE id == ?"
            self.execute_command_tuple(command, (id,))
            self.commit_changes()
            return f"Deleted person with id {id}"
        except Exception as e:
            return ("Delete error" + str(e))

    def execute_command(self,command):
        self.cur.execute(command)

    def execute_command_test(self,command):
        self.cur.execute(command)
    
    def execute_command_tuple(self,command, tuple):
        self.cur.execute(command, tuple)
    
    def commit_changes(self):
        self.con.commit()

