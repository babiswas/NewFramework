from Model import db
from Model.Testmodel import Account
from Route.route import account
from flask import request
from forms.forms import AccountForm
from flask import redirect
from flask import url_for   
from flask import render_template


@account.route('/add',methods=['GET','POST'])
def add_account():
        accountform=AccountForm(request.form)
        if request.method=="POST" and accountform.validate:
            name=request.form.get("name")
            accountid=request.form.get("accountid")
            clientid=request.form.get("clientid")
            clientsecret=request.form.get("clientsecret")
            refreshtoken=request.form.get("refreshtoken")
            enviroment_id=request.form.get("enviroment")
            account=Account(accountid,name,clientid,clientsecret,refreshtoken,int(enviroment_id))
            db.session.add(account)
            db.session.commit()
            return redirect(url_for("home.home"))
        return render_template("accountform.html",form=accountform)


@account.route('/read',methods=['GET'])
def account_list():
        try:
                myenviroment=request.args.get("myenviroment",None)
                if myenviroment==None:
                        page=request.args.get('page',1,type=int)
                        accountlist=Account.query.paginate(page=page,per_page=5)
                        next_url=url_for('account.account_list',page=accountlist.next_num) if accountlist.has_next else None
                        prev_url=url_for('account.account_list',page=accountlist.prev_num) if accountlist.has_prev else None
                        return render_template('account_list.html',accountlist=accountlist,next_url=next_url,prev_url=prev_url)
                else:
                        page=request.args.get('page',1,type=int)
                        accountlist=Account.query.filter_by(enviroment_id=int(myenviroment)).paginate(page=page,per_page=5)
                        next_url=url_for('account.account_list',page=accountlist.next_num) if accountlist.has_next else None
                        prev_url=url_for('account.account_list',page=accountlist.prev_num) if accountlist.has_prev else None
                        return render_template('account_list.html',accountlist=accountlist,next_url=next_url,prev_url=prev_url)
        except Exception as e:
                return render_template("Error.html")




@account.route('/edit/<int:accountid>',methods=['GET','POST'])
def update_account(accountid):
        accountobj=Account.query.get(accountid)
        accountform=AccountForm(obj=accountobj)
        if request.method=="POST" and accountform.validate:
            accountobj.clientid=request.form.get("clientid")
            accountobj.clientsecret=request.form.get("clientsecret")
            accountobj.refreshtoken=request.form.get("refreshtoken")
            db.session.commit()
            return redirect(url_for("home.home"))
        return render_template("add_account.html",form=accountform)


