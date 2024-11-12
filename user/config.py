
DIALCT = 'mysql'
DRITVER = 'pymysql'
HOST = 'mysql'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'makuiyu'
DBNAME = 'recharge_db'

SQLALCHEMY_DATABASE_URI = f'{DIALCT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:makuiyu@mysql/recharge_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
