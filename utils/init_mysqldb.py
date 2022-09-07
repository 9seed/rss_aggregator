import os
import contextlib

from config.settings import DB_SETTINGS
import MySQLdb as mysql
from DBUtils.PooledDB import PooledDB


class MysqlCli:

    def __init__(self):
        self.db_pool = PooledDB(mysql, 10, host=DB_SETTINGS['host'],
                                user=DB_SETTINGS['user'],
                                passwd=DB_SETTINGS['password'],
                                db=DB_SETTINGS['db'],
                                port=DB_SETTINGS['port'],
                                charset='utf8mb4')

    @contextlib.contextmanager
    def get_connection(self):
        con = self.db_pool.connection()
        try:
            yield con
        finally:
            pass

    def upsert(self, data):
        _id = data.get('_id', '')
        title = data.get('title', '')
        link = data.get('link', '')
        author = data.get('author', '')
        updated = data.get('updated', '')
        summary = data.get('summary', '')
        content = data.get('content', '')
        ts = data.get('ts', '')
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                SQL = f'''
                INSERT INTO RSS (ID, TITLE, LINK, AUTHOR, UPDATED, SUMMARY, CONTENT, TS) 
                VALUES ('{_id}', '{title}', '{link}', '{author}', '{updated}', '{summary}', '{content}', '{ts}')
                ON DUPLICATE KEY UPDATE ID = '{_id}'
                '''
                cursor.execute(SQL)
                conn.commit()
            except Exception as e:
                raise e


