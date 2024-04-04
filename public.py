from flask import*
from database import*



public=Blueprint('public',__name__)


@public.route('/')
def homepage():
    return render_template('home.html')


@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        username=request.form['uname']
        password=request.form['password']
        qry="select * from login where user_name='%s' and password='%s'"%(username,password)
        res=select(qry)
        

        if res:
            session['log']=res[0]['login_id']
            if res[0]['user_type']=='admin':
                return redirect(url_for('admin.admi'))
            elif res[0]['user_type']=='staff':
                return redirect(url_for('staff.staf'))
        else:
            return'''<script>alert("Inavalid username or password");window.location="/login"</script>'''
        
    
    
    return render_template('login.html')



@public.route('/forgotpassword',methods=['get','post'])
def forpass():
     if 'submit'in request.form:
        print("###############33")
        forgot=request.form['password']

        qry="select * from staff inner join login using(login_id) where user_name='%s' or phone_number='%s'"%(forgot,forgot)
        res=select(qry)
        if res:
            session['forgotpass']=res[0]['login_id']
            return'''<script>alert("");window.location="/confirm"</script>'''
    
     
     return render_template('forgotpassword.html')

@public.route('/confirm',methods=['get','post'])
def confirm():
    if 'submit'in request.form:
        password=request.form['password']
        confirm=request.form['newpassword'] 
        if password==confirm:
            qry="update login set password='%s' where login_id='%s'"%(confirm,session['forgotpass'])     
            update(qry)  
            return'''<script>alert("Password changed successfully");window.location="/login"</script>'''
        else:
            return'''<script>alert("password mismatching");window.location="/confirm"</script>'''



      


        



    return render_template('confirmpassword.html')








