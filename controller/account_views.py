from Model import db
from Model.Testmodel import Account,PrimeConfig,Testcase
from Route.route import account
from flask import request
from forms.forms import AccountForm
from flask import redirect
from flask import url_for   
from flask import render_template


@account.route('/<int:envid>/add',methods=['GET','POST'])
def add_account(envid):
        accountform=AccountForm(request.form)
        if request.method=="POST" and accountform.validate:
            name=request.form.get("name")
            accountid=request.form.get("accountid")
            clientid=request.form.get("clientid")
            clientsecret=request.form.get("clientsecret")
            refreshtoken=request.form.get("refreshtoken")
            account=Account(name,accountid,clientid,clientsecret,refreshtoken,envid)
            db.session.add(account)
            db.session.commit()
            return redirect(url_for("enviroment.Env_detail",envid=envid))
        return render_template("accountform.html",form=accountform)


@account.route('/read',methods=['GET'])
def account_list():
        page=request.args.get('page',1,type=int)
        accountlist=Account.query.paginate(page=page,per_page=5)
        next_url=url_for('account.account_list',page=accountlist.next_num) if accountlist.has_next else None
        prev_url=url_for('account.account_list',page=accountlist.prev_num) if accountlist.has_prev else None
        return render_template('account_list.html',accountlist=accountlist,next_url=next_url,prev_url=prev_url)


@account.route('/edit/<int:accountid>',methods=['GET','POST'])
def update_account(accountid):
        accountobj=Account.query.get(accountid)
        accountform=AccountForm(obj=accountobj)
        if request.method=="POST" and accountform.validate:
            accountobj.clientid=request.form.get("tags")
            accountobj.clientsecret=request.form.get("description")
            accountobj.refreshtoken=request.form.get("resourcePath")
            db.session.commit()
            return redirect(url_for("account.account_list"))
        return render_template("add_account.html",form=accountform)


@account.route('/read/<int:accountid>',methods=['GET'])
def Env_list(accountid):
      account=Account.query.get(id=accountid).first()
      tests=Testcase.query.get(acc_id=accountid).all()
      return render_template('enviroment.html',account=account,tests=tests)