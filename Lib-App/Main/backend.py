import sqlite3

def connect():
    connection  = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Book(ID INTEGER  PRIMARY KEY,Title TEXT, Author TEXT,Year INTEGER , ISBN INTEGER)")
    connection.commit()
    connection.close()

def insert(Title,Author,Year,ISBN):
    connection = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Book VALUES(NULL,?,?,?,?)",(Title,Author,Year,ISBN))
    connection.commit()
    connection.close()

def Veiw():
    connection = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Book")
    ROW = cursor.fetchall()
    connection.close()
    return ROW

def search(Title = "",Author = "",Year ="",ISBN =""):
    connection = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Book WHERE Title  = ? OR Author = ? OR Year = ? OR ISBN =?",
                   (Title,Author,Year,ISBN))
    ROW = cursor.fetchall()
    connection.close()
    return ROW
    

def delete(ID):
    connection = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Book WHERE ID = ? ", (ID,))
    connection.commit()
    connection.close()
    

def update(ID,Title,Author,Year,ISBN):
    connection = sqlite3.connect("LMS.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Book SET Title = ? ,Author = ? ,Year = ? ,ISBN = ?  WHERE  ID = ? ",(Title,Author,Year,ISBN,ID))
    connection.commit()
    connection.close()
    

