from flask import *
from database import *
from email.mime.text import MIMEText
import random
import smtplib
import string
from flask_mail import Mail

admin=Blueprint('admin',__name__)


@admin.route('/admi')
def admi():
    return render_template('admin.html')

@admin.route('/adminmanagestaff',methods=['get','post'])
def adminmanagestaff():
    if'submit'in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        phonenumber=request.form['phonenumber']
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']



        qry="insert into login values(null,'%s','%s','staff')"%(username,password)
        res=insert(qry)

        qry1="insert into staff values(null,'%s','%s','%s','%s','%s')"%(firstname,lastname,phonenumber,email,res)
        res1=insert(qry1)
        if res1:
            uname=request.form['username']
            password=request.form['password']
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('projectsriss2020@gmail.com','vroiyiwujcvnvade')
                print("##############")
              
                # msg = MIMEText("Your Password is {}".format(password,uname))
                message_body = "Hello Your Username is  {},\n\nYour Password is {}".format(uname, password)
                msg = MIMEText(message_body)
                msg['Subject'] = 'Registeration Completed '
                msg['To'] = email
                msg['From'] = 'projectsriss2020@gmail.com'

                gmail.send_message(msg)
                flash("A new password has been sent to your email address.")
                return redirect(url_for('admin.adminmanagestaff'))
            except Exception as ex:
                print("Couldn't send email", str(ex))
                flash("An error occurred while sending the OTP. Please try again later.")
                return redirect(url_for('admin.adminmanagestaff'))
            else:
                flash("The email and/or phone number you entered is incorrect. Please try again.")
                return redirect(url_for('public.home'))

    return render_template('adminmanagestaff.html')








@admin.route('/viewuser')
def viewuserr():
    data={}
    qry="select * from user"
    res=select(qry)
    data['view']=res
    return render_template('viewuser.html',data=data)



@admin.route('/viewpost')
def viewpost():
    data={}
    qry="select * from post inner join user using(user_id)"
    res=select(qry)
    data['view']=res
    return render_template('post.html',data=data)


@admin.route('/viewcommenta')
def viewcomment():
    data={}
    qry="select * from comment"
    res=select(qry)
    data['view']=res

    return render_template('comment.html',data=data)

@admin.route('/inactive')
def inactive():
    data={}
    qry="select * from staff inner join login using(login_id) where user_type='inactive'"
    res=select(qry)
    data['view']=res

    return render_template('inactive.html',data=data)


@admin.route('/viewcomplaint',methods=['get','post'])
def complaintt():
    data={}
    qry="select * from complaint"
    res=select(qry)
    data['view']=res
    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='update':
        qry="select * from complaint where complaint_id='%s'"%(id)
        res=select(qry)
        data['up']=res

    if 'submit' in request.form:
        reply=request.form['reply']

        q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
        update(q)

        return '''<script>alert("SEND SUCCESSFULLY...");window.location="/viewcomplaint"</script>'''

    return render_template("complaint.html",data=data)


@admin.route('/staffviewstaff',methods=['get','post'])
def staffviewstaff():
    data={}
    qry="select * from staff where login_id in(select login_id from login where user_type!='inactive')"
    res=select(qry)
    data['view']=res




    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='update':
        qry="select * from staff where staff_id='%s'"%(id)
        res=select(qry)
        data['up']=res
        if'update'in request.form:
            firstname=request.form['firstname']
            lastname=request.form['lastname']
            phonenumber=request.form['phonenumber']
            qry4="update staff set first_name='%s',last_name='%s',phone_number='%s' where staff_id='%s'"%(firstname,lastname,phonenumber,id)
            update(qry4)
            return'''<script>alert("UPDATED SUCCESSFULLY");window.location="/staffviewstaff"</script>'''

    if action=='delete':
        qry="update login set user_type='inactive' where login_id in(select login_id from staff  where staff_id='%s')"%(id)
        res=update(qry)
        data['up']=res    
        return'''<script>alert("DELETED SUCCESSFULLY");window.location="/staffviewstaff"</script>'''

    
    return render_template('staffviewstaff.html',data=data)





@admin.route('/notification',methods=['get','post'])
def notification():
    if 'SUBMIT'in request.form:
        noti=request.form['NOTIFICATION']

        qry="insert into notification values(null,'%s',curdate())"%(noti)
        res=insert(qry)
    return render_template("notification.html")                

  
        




@admin.route('/chat',methods=['post','get'])
def chat():
    data={}

    session['id']=request.args['id']
    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date , time"%(session['id'],session['log'],session['log'],session['id'])

    rg=select(f)
    print(rg)
   
    data['rg']=rg
   
    
    if'submit' in request.form:
        chat=request.form['chat']
 

        a="insert into chat values(null,'%s','admin','%s','staff','%s',curdate(),curtime())"%(session['log'],session['id'],chat)
        insert(a)
        return redirect(url_for('admin.chat',id=session['id']))
    
    return render_template("adminchat.html",data=data)