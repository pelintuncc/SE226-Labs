import mysql.connector

path = open("C:\\Users\\User\\Desktop\\Marvel.txt")

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
cursorObject = database.cursor()
cursorObject.execute("DROP DATABASE IF EXISTS newdatabase")
cursorObject.execute("CREATE DATABASE newdatabase")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="newdatabase",
    password="1234"
)
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("You are connected to the MySQL server", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database() ")
    record = cursor.fetchone()
    print("You are connected to the database", record)

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database='newdatabase',
        password="1234"
    )
    cursorObject = connection.cursor()
    cursorObject.execute("DROP TABLE IF EXISTS marvel")
    query = """CREATE TABLE marvel (
    ID INT,
    MOVIE VARCHAR(100),
    DATE VARCHAR(50),
    MCU_PHASE VARCHAR(100)
    )"""
    result = cursorObject.execute(query)
    print("marvel table created successfully.")
    cursorObject.execute("SHOW TABLES")

    for table_name in cursorObject:
        print(table_name)

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed")

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="newdatabase",
        password="1234"
    )
    CursorObject = connection.cursor()
    while path:
        text = path.readline()
        if text == "":
            break
        splitLines = text.split()
        Insert = """INSERT INTO marvel (ID, MOVIE, DATE, MCU_PHASE)
                 VALUES (%s, %s, %s, %s)"""
        record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
        CursorObject.execute(Insert, record)
        connection.commit()
    print("Records are added into Marvel table.")
    CursorObject.close()

    sql_select = "SELECT MOVIE FROM marvel"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_select)
    records = cursorObject.fetchall()
    for row in records:
        print(row)

    sql_remove = "DELETE FROM marvel WHERE MOVIE= 'TheIncredibleHulk'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_remove)
    connection.commit()

    sql_list = "SELECT * FROM marvel WHERE MCU_PHASE='Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_list)
    records2 = cursorObject.fetchall()
    for row2 in records2:
        print(row2)

    sql_update = "UPDATE marvel SET DATE= 'November 3, 2017' WHERE MOVIE='Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_update)
    connection.commit()

except mysql.connector.Error as error:
    print("Failed to insert record into marvel table {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed.")