from wtforms import Form,StringField,SelectField


class TestForm(Form):
        id=StringField("TestId")
        tags=StringField("TestTag")
        description=StringField("Description")
        resourcePath=StringField("ResourcePath")
        method=StringField("Method")
        role=SelectField('Role',choices=[('admin','ROLE_ADMIN'),('learner','ROLE_LEARNER')])


class AccountForm(Form):
        name=StringField("Name")
        clientid=StringField("Client Id")
        clientsecret=StringField("Client Secret")
        refreshtoken=StringField("Refresh Token")


class TestData(Form):
        tags=StringField("TestTag")
        description=StringField("Description")
        resourcePath=StringField("ResourcePath")
        method=StringField("Method")
        role=SelectField('Role',choices=[('admin','ROLE_ADMIN'),('learner','ROLE_LEARNER')])
            