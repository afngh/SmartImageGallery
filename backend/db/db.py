import sqlite3
import os
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
    CREATE TABLE image_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_path TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_images_table)
    except Exception as e:
        print(e)

def insert_image(conn, image_path,counter):
    sql = """
    INSERT INTO image_data(id,image_path) VALUES(?,?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (counter,image_path))
        conn.commit()
    except Exception as e:
        print("error : ",e)

def insert_images_from_folder(conn, folder_path):
    counter = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            insert_image(conn, image_path,counter)
            counter += 1
            print(f"Inserted : {counter} image : {image_path}")

if __name__ == "__main__":
    conn = create_connection("gallery.db")
    create_table(conn)
    insert_images_from_folder(conn, "../data/")