import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="N1610J2803C2912s?",
    database = "LaPlateforme"
)
cursor = db.cursor()
requete = "SELECT nom, capacite FROM salles"
cursor.execute(requete)


cursor.close()
db.close()