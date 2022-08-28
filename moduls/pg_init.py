import os
import json
from dotenv import load_dotenv

import contextlib
import psycopg2
import psycopg2.pool as pool

load_dotenv('.env')


class PGCli:

    def __init__(self):
        self.db_pool = pool.SimpleConnectionPool(minconn=1,
                                                 maxconn=10,
                                                 host=os.environ['HOST'],
                                                 database=os.environ['DB_NAME'],
                                                 user=os.environ['DB_USER'],
                                                 password=os.environ['DB_PASSWORD'],
                                                 port=os.environ['PORT'])

    @contextlib.contextmanager
    def get_connection(self):
        con = self.db_pool.getconn()
        try:
            yield con
        finally:
            self.db_pool.putconn(con)

    def update_news(self, **kwargs):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                sql = '''
                INSERT INTO news
                (title, title_detail, id, guidislink, link, links, updated, updated_parsed, content, summary, authors, author_detail, author)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id)
                DO UPDATE SET ( updated, updated_parsed) values (%s,%s) 
                '''
                cursor.execute(sql, (kwargs.get('title'),
                                     kwargs.get('title_detail'),
                                     kwargs.get('id'),
                                     kwargs.get('guidislink'),
                                     kwargs.get('link'),
                                     kwargs.get('links'),
                                     kwargs.get('updated'),
                                     kwargs.get('updated_parsed'),
                                     kwargs.get('content'),
                                     kwargs.get('summary'),
                                     kwargs.get('authors'),
                                     kwargs.get('author_detail'),
                                     kwargs.get('author'),
                                     kwargs.get('updated'),
                                     kwargs.get('updated_parsed')))
            except psycopg2.Error as error:
                raise f'Database error: {error}'
            except Exception as ex:
                raise f'General error: {ex}'