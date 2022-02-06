from Model import db
from Model.Testmodel import Report
from Route.route import report
from flask import request
from flask import jsonify
import copy

@report.route('/add',methods=['POST'])
def create_report():
    try:
        report_data=request.get_json()
        new_report=Report(report_data["testcase_id"],report_data["enviroment_id"],report_data["account_id"],report_data["verdict"])
        db.session.add(new_report)
        db.session.commit()
    except Exception as e:
        return jsonify({"response":"BADREQUEST"})


@report.route('/read',methods=['GET'])
def read_report():
    try:
        reports=Report.query.all()
        report_list=list()
        for report in reports:
            report=copy.deepcopy(["testcaseId","enviromentId","accountId","verdict"])
            report_list.append(dict(zip(report,[report.testcase_id,report.enviroment_id,report.account_id,report.verdict])))
        return jsonify(report_list)
    except Exception as e:
        return jsonify({"response":"BADREQUEST"})


@report.route('/update/<int:testcase_id>',methods=['PATCH'])
def update_report(testcase_id):
    try:
        data=request.get_json()
        report=Report.query.get(testcase_id)
        report.enviroment_id=data["enviromentId"]
        report.verdict=data["verdict"]
        report.account_id=data["account_id"]
        db.session.commit()
        return jsonify({"response":"SUCCESS"})
    except Exception as e:
        return jsonify({"response":"BADREQUEST"})






