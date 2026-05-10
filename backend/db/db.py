import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn):
    sql_create_images_table = """
    CREATE TABLE images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_path TEXT,
        image_embedding BLOB
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_images_table)
    except Exception as e:
        print(e)

def insert_image(conn, image_path, image_embedding):
    sql = """
    INSERT INTO images(image_path, image_embedding) VALUES(?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (image_path, image_embedding))
        conn.commit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_connection("gallery.db")
    create_table(create_connection("gallery.db"))