import sqlite3


class DbManager:

    def create_connection(self, db_file):
    
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            pass
             #retry
        return conn
        
    def execute_query(self, query):

        conn = self.create_connection("test.sqlite3")
        cursor_obj = conn.cursor()
        cursor_obj.execute(query)
    
    def create_tables(self):

        create_photos = """CREATE TABLE "photos" ( "id"	INTEGER, "width" INTEGER, "height" INTEGER, "url" NUMERIC, "photographer"	TEXT, "photograher_url"	TEXT, "photographer_id"	INTEGER, "avg_color" TEXT, "liked" INTEGER, "alt" TEXT  PRIMARY KEY("id") );"""
        create_photo_sources = """CREATE TABLE "photo_sources" ( "type"	TEXT, "url"	TEXT, "photo_id"	INTEGER, "photo_source_id"	INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY("photo_id") REFERENCES "photos"("id") );"""
        self.execute_query(create_photos)
        self.execute_query(create_photo_sources)