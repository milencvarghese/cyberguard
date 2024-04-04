from flask import*
from admin import admin
from public import public
from staff import staff
from api import api

app=Flask(__name__)
app.secret_key="kkk"



import smtplib      
from email.mime.text import MIMEText
from flask_mail import Mail

mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = 'vroiyiwujcvnvade'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(staff)
app.register_blueprint(api)

app.run(debug=True,port=5013,host="0.0.0.0")

