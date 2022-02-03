from Model.Testmodel import Enviroment
from Route.route import enviroment
from flask import request
from flask import url_for   
from flask import render_template


@enviroment.route('/read',methods=['GET'])
def enviroment_list():
      page=request.args.get('page',1,type=int)
      enviroments=Enviroment.query.paginate(page=page,per_page=5)
      next_url=url_for('enviroment.enviroment_list',page=enviroments.next_num) if enviroments.has_next else None
      prev_url=url_for('enviroment.enviroment_list',page=enviroments.prev_num) if enviroments.has_prev else None
      return render_template('enviroment_list.html',enviroments=enviroments,next_url=next_url,prev_url=prev_url)

