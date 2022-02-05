from Model import db
from sqlalchemy.dialects.postgresql import JSON

class Testcase(db.Model):
        __tablename__="testcase"
        testcase_id=db.Column(db.String(20),nullable=False,unique=True,primary_key=True)
        test_tags=db.Column(db.String(100),nullable=False,unique=True)
        test_description=db.Column(db.String(150),nullable=False)
        resource_path=db.Column(db.String(150),nullable=False)
        http_method=db.Column(db.String(20),nullable=False)
        role=db.Column(db.String(20),nullable=False)
        testdata=db.relationship("Testdata",backref="testdata_testcase")

        def __str__(self):
            return f"{self.testcase_id} {self.test_description}"

        def __init__(self,test_id,test_tag,description,resourcepath,method,role):
            self.testcase_id=test_id
            self.test_tags=test_tag
            self.test_description=description
            self.resource_path=resourcepath
            self.http_method=method
            self.role=role


class Enviroment(db.Model):
        __tablename__="enviroment"
        enviroment_id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
        enviroment_name=db.Column(db.String(100),nullable=False)
        enviroment_description=db.Column(db.String(100),nullable=False)
        enviroment_url=db.Column(db.String(100),nullable=False)
        account=db.relationship("Account",backref="primeaccount")
        testdata=db.relationship("Testdata",backref="testdata_enviroment",uselist=False)

        def __str__(self):
            return f"{self.enviroment_id} {self.enviroment_url}"

        def __init__(self,enviromenturl):
            self.enviroment_url=enviromenturl


class Account(db.Model):
        __tablename__="account"
        account_id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
        account_name=db.Column(db.String(100),nullable=False)
        clientid=db.Column(db.String(100),nullable=False)
        clientsecret=db.Column(db.String(100),nullable=False)
        refreshtoken=db.Column(db.String(100),nullable=False)
        enviroment_id=db.Column(db.Integer,db.ForeignKey('enviroment.enviroment_id'))
        testdata=db.relationship("Testdata",backref="testdata_account",uselist=False)

        def __str__(self):
            return f"{self.enviroment_id} {self.account_name}"

        def __init__(self,account_id,account_name,clientid,clientsecret,refreshtoken,enviroment_id):
            self.account_id=account_id
            self.account_name=account_name
            self.clientid=clientid
            self.clientsecret=clientsecret
            self.refreshtoken=refreshtoken
            self.enviroment_id=enviroment_id


class Testdata(db.Model):
        __tablename__="testdata"
        testdata_id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
        test_data=db.Column(JSON)
        testcase_id=db.Column(db.String(20),db.ForeignKey('testcase.testcase_id'))
        account_id=db.Column(db.Integer,db.ForeignKey('account.account_id'))
        enviroment_id=db.Column(db.Integer,db.ForeignKey('enviroment.enviroment_id'))


        def __init__(self,test_data,test_id,account_id,enviroment_id):
            self.test_data=test_data
            self.testcase_id=test_id
            self.account_id=int(account_id)
            self.enviroment_id=enviroment_id

        def __str__(self):
            return f"{self.test_data}"





    
   
