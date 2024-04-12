import database as db
from Employes import Employe

class EmployeDao:
    connexion = db.connect_db()
    cursor = connexion.cursor()
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employe"
        EmployeDao.cursor.execute(sql)
        try:
            employes = EmployeDao.cursor.fetchall()
            message = "success"
        except Exception as err:
            employes = []
            message = "error"
        return employes, message
    
    @classmethod
    def add(cls,emp:Employe):
        sql = "INSERT INTO employe (nom, prenom, matricule, fonction, departement) VALUES (%s,%s,%s,%s,%s)"
        params = (emp.nom,emp.prenom,emp.matricule,emp.fonction,emp.departement)
        try:
            EmployeDao.cursor.execute(sql,params)
            EmployeDao.connexion.commit()
            message = "success"
        except Exception as ex:
            message = "error"
        return message
    
    @classmethod
    def get_one(cls,matricule):
        sql = "SELECT * FROM employe WHERE matricule=%s"
        try:
            EmployeDao.cursor.execute(sql, (matricule,))
            message = "euccess"
            employe = EmployeDao.cursor.fetchone()
        except Exception as ex:
            message = "erreur lors de la recherche"
            employe = []
        return (message,employe)