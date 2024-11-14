
import os


USER_SERVICE_HOST = os.environ.get('USER_SERVICE_HOST', 'localhost')
USER_SERVICE_PORT = os.environ.get('USER_SERVICE_PORT', '5001')

ORDER_SERVICE_HOST = os.environ.get('ORDER_SERVICE_HOST', 'localhost')
ORDER_SERVICE_PORT = os.environ.get('ORDER_SERVICE_PORT', '5002')

INVENTORY_SERVICE_HOST = os.environ.get('INVENTORY_SERVICE_HOST', 'localhost')
INVENTORY_SERVICE_PORT = os.environ.get('INVENTORY_SERVICE_PORT', '5003')

PAYMENT_SERVICE_HOST = os.environ.get('PAYMENT_SERVICE_HOST', 'localhost')
PAYMENT_SERVICE_PORT = os.environ.get('PAYMENT_SERVICE_PORT', '5004')
