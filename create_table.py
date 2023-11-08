def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS Phones (
        phoneID INTEGER PRIMARY KEY,
        contactName VARCHAR(255),
        phoneValue VARCHAR(255)
        );
        """
    cur.execute(sql)

    con.commit()
    con.close()
