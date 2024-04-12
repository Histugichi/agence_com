from flask import Flask, render_template, request, session, url_for, redirect
from Employes.Employe import Employe
import departement as departement
from Employes.employe_dao import EmployeDao
from users.users import User
from users.user_dao import Userdao


app = Flask(__name__)
app.secret_key='secretkey'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    req = request.form
    message=None
    User=None
    if  request.method == 'POST':
        username = req['username']
        password = req['password']
        if username == '' or password == '':
            message= 'error'
        else:
           (message, password) = Userdao.get_one(username, password)  
           if message=='success':
              session['username'] = User[2]
              session['nom_complet'] =User[1]
              return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/employe")
def employes():
    employes = EmployeDao.get_all()
    return render_template("employe.html", employes=employes)

@app.route("/users")
def User():
    return render_template("user.html")
    

@app.route("/add-employe", methods = ['POST', 'GET'])
def add_employe():
    req = request.form
    message=None
    employe=None
    if request.method == 'POST':
        nom= req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        departement = req['departement']
        if nom=="" and prenom=="" and matricule=="" and fonction=="" and departement=="": 
            message='error'
        else:
             employe = Employe(nom,prenom,matricule,fonction,departement)
        #print(employe.nom,employe.prenom,employe.matricule,employe.fonction,employe.departement)
    return render_template("add_employe.html",employe=employe,message=message)

@app.route("/departements")
def departements():
    departements = departement.dliste()
    return render_template("departements.html", departements=departements)

@app.route("/add-departements")
def add_departements():
    return render_template("add_departements.html")