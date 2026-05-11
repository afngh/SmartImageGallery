import sqlite3
import os

class GalleryDB:
    def __init__(self, db_file="db/gallery.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_image_path(self, image_ids):
        image_id = str(tuple(image_ids))
        self.cursor.execute(f"SELECT image_path FROM image_data WHERE id in {image_id}")
        data_list =  self.cursor.fetchall()
        return [i[0] for i in data_list]


if __name__ == "__main__":
    gallery_db = GalleryDB()
    print(gallery_db.get_image_path((1,5,8,3,2)))