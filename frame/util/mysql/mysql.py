from frame.config.read_config import read_config
import MySQLdb

from util.logger import logger


class MySQLClient:
    def __init__(self):
        self.cursor = None
        self.db = None
        self.host = read_config.get_mysql_host()
        self.port = int(read_config.get_mysql_port())
        self.user = read_config.get_mysql_user()
        self.password = read_config.get_mysql_password()
        self.database = read_config.get_mysql_db()

    def connect(self):
        try:
            self.db = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, database=self.database, charset='utf8')
            self.cursor = self.db.cursor()
            logger.info('Connected to MySQL')
        except Exception as e:
            self.db.rollback()
            logger.error(f"Fail to connect to MySQL:{e}")