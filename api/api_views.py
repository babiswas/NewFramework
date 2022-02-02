from Model import db
from flask import jsonify
from Route.route import api
from Model.Testmodel import Testdata,Testcase
from flask import request


@api.route('/getdata/<testid>',methods=['GET'])
def get_data(testid):
        try:
            data=Testdata.query.get(testid)
            if data:
                return jsonify(data.primedata)
            else:
                raise Exception
        except Exception as e:
            return jsonify({"response":"BAD REQUEST"})




@api.route('/adddata',methods=['POST'])
def set_data():
        try:
            data=request.get_json()
            testid=data["id"]
            object=Testcase.query.get(testid)
            if object:
                obj=Testdata(data["id"],data["primedata"])
                db.session.add(obj)
                db.session.commit()
                return jsonify({"response":"SUCCESS"})
        except Exception as e:
            return jsonify({"response":"BAD REQUEST"})