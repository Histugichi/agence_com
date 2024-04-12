import database as db

def dliste():
    connexion = db.connect_db()
    cursor = connexion.cursor()
    sql = "SELECT * FROM departement"
    cursor.execute(sql)
    resultats = cursor.fetchall()
    cursor.close()
    
    return resultats