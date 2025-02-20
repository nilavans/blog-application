from db.connection import create_tables
from manager import *

# It will create all the necessary tables.
create_tables()

manager = Manager()
manager.run()