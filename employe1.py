import database as db

def liste():
    connexion = db.connect_db()
    cursor = connexion.cursor()
    sql = "SELECT * FROM employe"
    cursor.execute(sql)
    resultats = cursor.fetchall()
    cursor.close()
    
    return resultats