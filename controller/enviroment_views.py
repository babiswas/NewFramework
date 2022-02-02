from Model import db
from Model.Testmodel import Account,PrimeConfig
from Route.route import enviroment
from flask import request
from forms.forms import AccountForm
from flask import url_for   
from flask import render_template
from flask import redirect


@enviroment.route('/read',methods=['GET'])
def enviroment_list():
      page=request.args.get('page',1,type=int)
      enviroments=PrimeConfig.query.paginate(page=page,per_page=5)
      next_url=url_for('enviroment.enviroment_list',page=enviroments.next_num) if enviroments.has_next else None
      prev_url=url_for('enviroment.enviroment_list',page=enviroments.prev_num) if enviroments.has_prev else None
      return render_template('enviroment_list.html',enviroments=enviroments,next_url=next_url,prev_url=prev_url)



@enviroment.route('/read/<int:envid>',methods=['GET','POST'])
def Env_detail(envid):
            enviroment=PrimeConfig.query.get(envid)
            accounts=Account.query.filter_by(env_id=envid).all()
            return render_template("enviroment.html",accounts=accounts,enviroment=enviroment)


