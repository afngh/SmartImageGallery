import sqlite3
import os

def get_image_path(image_ids,db_file="db/gallery.db"):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    image_id = str(tuple(image_ids))
    cursor.execute(f"SELECT image_path FROM image_data WHERE id in {image_id}")
    data_list = cursor.fetchall()
    return [i[0] for i in data_list]

if __name__ == "__main__":
    print(get_image_path((1,5,8,3,2)))