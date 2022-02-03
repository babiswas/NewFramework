from wtforms import Form,StringField,SelectField,TextAreaField


class TestForm(Form):
        id=StringField("TestId")
        tags=StringField("TestTag")
        description=StringField("Description")
        resourcePath=StringField("ResourcePath")
        method=StringField("Method")
        role=SelectField('Role',choices=[('ROLE_ADMIN','ADMIN'),('ROLE_LEARNER','LEARNER')])


class AccountForm(Form):
        name=StringField("Name")
        clientid=StringField("Client Id")
        clientsecret=StringField("Client Secret")
        refreshtoken=StringField("Refresh Token")
        enviroment=SelectField('Enviroment',choices=[(1,'QE'),(2,'STAGE1'),(3,'STAGE4'),(4,'STAGE'),(5,'AZ'),(6,'APAC'),(7,'PROD'),(8,'EU')])


class TestData(Form):
        testcaseid=StringField("Testid")
        jsondata=TextAreaField("Jsondata")
        account_id=StringField("Accountid")
        enviroment_id=SelectField('Enviroment',choices=[(1,'QE'),(2,'STAGE1'),(3,'STAGE4'),(4,'STAGE'),(5,'AZ'),(6,'APAC'),(7,'PROD'),(8,'EU')])
            