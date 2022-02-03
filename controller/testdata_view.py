from Model import db
from Model.Testmodel import Testdata
from forms.forms import TestDataForm
from Route.route import testdata
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template


@testdata.route('/add',methods=['GET','POST'])
def test_data_add():
        testdataform=TestDataForm(request.form)
        if request.method=="POST" and testdataform.validate:
                testcaseid=request.form.get("testcaseid")
                account_id=request.form.get("account_id")
                enviroment_id=request.form.get("enviroment_id")
                jsondata=request.form.get("jsondata")
                testdata=Testdata(jsondata,testcaseid,account_id,enviroment_id)
                db.session.add(testdata)
                db.session.commit()
                return redirect(url_for("testdata.test_data_list"))
        return render_template("add_test_data.html",form=testdataform)


@testdata.route('/read',methods=['GET'])
def test_data_list():
      testdata=Testdata.query.all()
      return render_template('test_data_list.html',testdata=testdata)


@testdata.route('/edit/<testid>',methods=['GET','POST'])
def edit_test_data(testid):
        testdata=Testdata.query.get(testid)
        testdataform=TestDataForm(obj=testdata)
        if request.method=="POST" and testdataform.validate:
               testdata.testcase_id=request.form.get("testcaseid")
               testdata.account_id=request.form.get("account_id")
               testdata.enviroment_id=request.form.get("enviroment_id")
               testdata.test_data=request.form.get("jsondata")
               db.session.commit()
               return redirect(url_for("testdata.read"))
        return render_template("add_test_data.html",form= testdataform)

   
       


