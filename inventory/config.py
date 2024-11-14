
import os

DIALECT = os.environ.get('MYSQL_DIALECT', 'mysql')
DRITVER = os.environ.get('MYSQL_DRITVER', 'pymysql')
HOST = os.environ.get('MYSQL_HOST', 'localhost')
PORT = os.environ.get('MYSQL_PORT', '30306')
USERNAME = os.environ.get('MYSQL_USERNAME', 'root')
PASSWORD = os.environ.get('MYSQL_PASSWORD', 'makuiyu')
DBNAME = os.environ.get('MYSQL_DBNAME', 'recharge_db')

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:makuiyu@mysql:3306/recharge_db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:makuiyu@localhost:30306/recharge_db'
SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
