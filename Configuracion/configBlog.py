import os	

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
PWD = os.path.abspath(os.curdir)	
DEBUG = True
DB_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="root", password="", hostname="localhost", databasename="gqcurso5x")
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

#app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

