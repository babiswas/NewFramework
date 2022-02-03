from flask import render_template
from Route.route import home
from Model.Testmodel import Enviroment,Account,Testcase

@home.route('/')
def home():
    enviroments=Enviroment.query.limit(5).all()
    print(enviroments)
    accounts=Account.query.limit(5).all()
    testcases=Testcase.query.limit(5).all()
    return render_template("home.html",enviroments=enviroments,accounts=accounts,testcases=testcases)






