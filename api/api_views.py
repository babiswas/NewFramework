from Model import db
from flask import jsonify
from Route.route import api
from Model.Testmodel import Testdata,Testcase
from flask import request
import copy


@api.route('/getdata/<testid>',methods=['GET'])
def get_data(testid):
        try:
            data=Testdata.query.get(testid)
            if data:
                return jsonify(data.test_data)
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


@api.route('/alltest/<enviroment>',methods=['GET'])
def get_all_tests(enviroment):
    try:
        data=db.engine.execute('SELECT testdata.test_data,testdata.testcase_id,account.account_id,account.clientid,account.clientsecret,account.refreshtoken,account.enviroment_id,testcase.resource_path FROM testdata INNER JOIN account on account.account_id=testdata.account_id  INNER JOIN testcase on testcase.testcase_id=testdata.testcase_id WHERE account.enviroment_id=1;')
        tests=list()
        for record in data:
            l=copy.deepcopy(["data","testId","accountId","clientId","clientSecret","refreshToken","enviromentId","resourcePath"])
            tests.append(dict(zip(l,list(record))))
        return jsonify(tests)
    except Exception as e:
        return jsonify({"response":"BADREQUEST"})