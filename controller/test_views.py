from Model import db
from Model.Testmodel import Testcase
from Route.route import testcase
from flask import request
from forms.forms import TestForm
from flask import redirect
from flask import url_for
from flask import render_template

@testcase.route('/add',methods=['GET','POST'])
def add_create_tests():
      testform=TestForm(request.form)
      if request.method=="POST" and testform.validate:
         testid=request.form.get("id")
         testtag=request.form.get("tags")
         testdescription=request.form.get("description")
         testresource=request.form.get("resourcePath")
         mthd=request.form.get("method")
         role=request.form.get("role")
         testcase=Testcase(testid,testtag,testdescription,testresource,mthd,role)
         db.session.add(testcase)
         db.session.commit()
         return redirect(url_for("home.home"))
      return render_template("add_test.html",form=testform)


@testcase.route('/read',methods=['GET'])
def test_list():
      testlist=Testcase.query.all()
      return render_template('test_list.html',testlist=testlist)


@testcase.route('/edit/<testid>',methods=['GET','POST'])
def edit_test(testid):
            testobj=Testcase.query.get(testid)
            testform=TestForm(obj=testobj)
            testform.tags.data=testobj.test_tags
            testform.description.data=testobj.test_description
            testform.method.data=testobj.http_method
            if request.method=="POST" and testform.validate:
                  testobj.test_tags=request.form.get("tags")
                  testobj.test_description=request.form.get("description")
                  testobj.resource_path=request.form.get("resourcePath")
                  testobj.http_method=request.form.get("method")
                  testobj.role=request.form.get("role")
                  db.session.commit()
                  return redirect(url_for("home.home"))
            return render_template("edit_test.html",form=testform)
   
       


