from flask import render_template
from Route.route import home
from Model.Testmodel import PrimeConfig,Account

@home.route('/')
def home():
    enviroments=PrimeConfig.query.all()
    return render_template("home.html",enviroments=enviroments)






