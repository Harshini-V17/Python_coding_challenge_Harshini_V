import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=HARSHU\\SQLEXPRESS;'
                            'Database=system;'
                            'Trusted_Connection=yes;')
            return conn
        except:
            print("Connection failed")