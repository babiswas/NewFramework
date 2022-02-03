from flask import render_template
from Route.route import home
from Model.Testmodel import Enviroment

@home.route('/')
def home():
    enviroments=Enviroment.query.all()
    return render_template("home.html",enviroments=enviroments)






