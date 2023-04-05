import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="N1610J2803C2912s?",
    database = "LaPlateforme"
)
cursor = db.cursor()
cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")
result = cursor.fetchone()[0]


print("La superficie de La Plateforme est de {} m²".format(result))


db.close()