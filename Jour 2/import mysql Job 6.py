import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="N1610J2803C2912s?",
    database = "LaPlateforme"
)
cursor = db.cursor()
cursor.execute("SELECT SUM(capacite) AS capacite_totale FROM salles")
result = cursor.fetchone()

capacite_totale = result[0]
print("La capacité totale des salles est de {}".format(capacite_totale))


db.close()