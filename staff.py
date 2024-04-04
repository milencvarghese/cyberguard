from flask import *
from database import *

staff=Blueprint('staff',__name__)


@staff.route('/staff')
def staf():
    return render_template('staff.html')


@staff.route('/staffviewuser')
def viewuserr():
    data={}
    qry="select * from user"
    res=select(qry)
    data['view']=res
    return render_template('staffviewuser.html',data=data)



@staff.route('/staffviewpost')
def viewpost():
    data={}
    qry="select * from post inner join user using(user_id)"
    res=select(qry)
    data['view']=res
    return render_template('staffpost.html',data=data)






@staff.route('/staffviewcomment')
def viewcomment():
    id=request.args['id']
    data={}
    qry="select * from comment inner join user using(login_id) where post_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template('staffcomment.html',data=data)


@staff.route('/staffviewcomplaint',methods=['get','post'])
def complaintt():
    data={}
    qry="select * from complaint inner join user using(user_id)"
    res=select(qry)
    data['view']=res

    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from complaint where complaint_id='%s'"%(id)
        res1=select(qry1)
        data['up']=res1
        print(res1,"ppppppppppppppppppppppppppppppp")


    if 'submit' in request.form:
            reply=request.form['reply']

            q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
            update(q)

            return '''<script>alert("SEND SUCCESSFULLY...");window.location="/staffviewcomplaint"</script>'''

    return render_template("staffcomplaint.html",data=data)



@staff.route('/staffchat',methods=['get','post'])
def staffchat():
    data={}
    qry="select * from login where user_type='admin'"
    res=select(qry)
    if res:
        adminid=res[0]['login_id']
        name=res[0]['user_type']
    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date , time"%(session['log'],adminid,adminid,session['log'])

    rg=select(f)
    print(rg)
   
    data['rg']=rg
   
  
    
    if'submit' in request.form:
        chat=request.form['chat']
 

        a="insert into chat values(null,'%s','staff','%s','admin','%s',curdate(),curtime())"%(session['log'],adminid,chat)
        insert(a)
        return redirect(url_for('staff.staffchat'))
    return render_template('staffchat.html',data=data,name=name)


@staff.route('/notification',methods=['get','post'])
def notification():
    if 'SUBMIT'in request.form:
        noti=request.form['NOTIFICATION']

        qry="insert into notification values(null,'%s',curdate())"%(noti)
        res=insert(qry)
    return render_template("notification.html")     
