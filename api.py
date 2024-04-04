import os
from flask import *
from database import *


api=Blueprint('api',__name__)

@api.route('/reg',methods=['get','post'])
def apk():
    data={}
    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    username=request.args['username']
    password=request.args['password']


    qry="insert into login values(null,'%s','%s','user')"%(username,password)
    res=insert(qry)


    qry2="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,phone,email)
    res2=insert(qry2)
    if res2:
        data['status']="success"

    return str(data)


@api.route('/logins',methods=['get','post'])
def logins():
    data={}
    print("################3")
    username=request.args['uname']
    password=request.args['pword']

    qry="select * from login where user_name='%s' and password='%s'"%(username,password)
    res=select(qry)
    print("//////////////////",res)

    if res:
        data['status']="success"
        data['data']=res

    else:
        data['status']='failed'
    return str(data)



@api.route("/view_post")
def view_post():
    data={}

    qry="select * from post inner join user using(user_id)"
    res=select(qry)

    if res:
        data['status']="success"
        data['data']=res

    else:
        data['status']='failed'
    data['method']="post"
    return str(data)


@api.route("/comp")
def complaint():
    data={}
    com=request.args['complaint']
    id=request.args['id']

    qry="insert into complaint values(null,'%s','%s','pending',curdate())"%(id,com)
    res=insert(qry)
    if res:
        data['status']="success"

    else:
        data['status']='failed'
    data['method']='send_complaint'
    return str(data)






@api.route("/viewcom")
def viewcomplaint():
    data={}
    id=request.args['id']

    qry="select * from complaint where user_id='%s'"%(id)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)

        

@api.route('/view',methods=['get','post'])
def notification():
    data={}
    qry="select * from notification where date_time=curdate()"
    res=select(qry)
    print(res,"sdfghu")
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)




import uuid
# @api.route('/managepost',methods=['get','post'])
# def mpost():
#     data={}
#     print("###############")
   
#     image=request.files['images']
    
#     print("123456789")

#     path="static/" +str(uuid.uuid4())+image.filename
#     image.save(path)
    
#     post=request.form['cy_post']
#     id=request.form['logid']


#     ww="select user_id from user where login_id='%s'"%(id)
#     r=select(ww)
#     userid=r[0]['user_id']

#     qry="insert into post values(null,'%s','%s','%s')"%(userid,post,path)
#     res=insert(qry)

#     if res:
#         data['status']="success"

#     return str(data)

@api.route('/managepost',methods=['get','post'])
def managepost():
    data={}
    print("PPPPPPPPPPPPPPPPPP")
    ppost=request.form['cy_post']
    id=request.form['logid']
    print("ppkkkkkk",ppost,id)
    path=request.files['image']
    print("###############",path)
    img="static/"+str(uuid.uuid4())+path.filename
    path.save(img)
    q="select * from user where login_id='%s'"%(id)
    r=select(q)
    if r:
        a=r[0]['user_id']
    
        
        qry="insert into post values(null,'%s','%s','%s',curdate(),'pending')"%(a,ppost,img)
        insert(qry)
        data['status']="success"
    
    return str(data)





@api.route('/chatnew',methods=['get','post'])
def chat():
    data={}
    
    chat=request.args['chat']
    receiver_id=request.args['receiver_id']
    sender_id=request.args['sender_id']


    
    print(sender_id,'/////////////////////////////////////////////////')
    
    
    qry="insert into chat values(null,'%s','user','%s','user','%s',curdate(),curtime())"%(sender_id,receiver_id,chat)
    res=insert(qry)
    if res:
        data['status']="success"
        
        data['method']="done"
        
        
        
    return str(data)


@api.route('/viewchat1')
def viewchat():
    user_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']

    
    data={}


    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY time and date"%(user_id,receiver_id,receiver_id,user_id)
    rg=select(f)
    print(rg,"//////////////////////////?????????")
    if rg:
        data['status']="success"
        data['data']=rg
    data['method']="view"

    
    

    return str(data)  


@api.route("/viewcomments")
def viewcomment():
    data={}
    # loginid=request.args['loginid']
    id=request.args['id']

    qry="select * from comment left join user using(login_id) where post_id='%s' and type='normal'"%(id)
    res=select(qry)
    print(res,"///////////////////////")
    if res:
        data['status']="success"
        data['data']=res
    data['method']='comment'
    return str(data)









@api.route('/comment',methods=['get','post'])
def comment():
    data={}
    
    id=request.args['id']
    # user_id=request.args['userid']
    login_id=request.args['loginid']
    comment=request.args['comment']
    # cmm = predictfn(comment)
    import nltk
    from sklearn.model_selection import train_test_split

    # path1 = "E:\\New folder (7)\\cyber\\myapp\\cyberbullying-bdlstm.h5"
    # path1="C://final_backup//Cyberbullying_Md_Bca//Cyber_web//cyberbullying-bdlstm.h5"
    # path1 = "//cyberbullying-bdlstm.h5"
    # path1="C://final_backup//Cyberbullying_Md_Bca//Cyber_web//cyberbullying-bdlstm.h5"
    path1="C://Users//User//Desktop//New folder//cyber_guard//cyberbullying-bdlstm.h5"
    # C:\Users\User\Desktop\New folder\cyber_guard\cyberbullying-bdlstm.h5
    

    # path1 = "E:\\New folder (7)\\cyber\\cyber\\static\\cyberbullying_tweets.csv"
    # path2 = "E:\\New folder (7)\\cyber\\myapp\\tokenizer.json"
    path2="C://Users//User//Desktop//New folder//cyber_guard//tokenizer.json"
    # C:\Users\User\Desktop\New folder\cyber_guard\tokenizer.json

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import json

    import tensorflow as tf
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.callbacks import EarlyStopping

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(2000, 64),  # embedding layer
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, dropout=0.2, recurrent_dropout=0.2)),  # LSTM layer
        tf.keras.layers.Dropout(rate=0.2),  # dropout layer
        tf.keras.layers.Dense(64, activation='swish'),  # fully connected layer
        tf.keras.layers.Dense(1, activation='sigmoid')  # final layer
    ])

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'AUC'])

    model.load_weights(path1)
    print("ok")
    #
    #
    # tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=2000, oov_token="<OOV>")
    #
    # tokenizer.



    import functools, re
    import random

    df = pd.read_csv("static//cyberbullying_tweettss.csv")
    df.cyberbullying_type.value_counts().plot.barh(xlim=(7800, 8000))

    stopwords = [i.lower() for i in nltk.corpus.stopwords.words('english') + [chr(i) for i in range(97, 123)]]
    x = df.tweet_text.apply(lambda text: re.sub("\s+", " ", ' '.join([i for i in re.sub("[^9A-Za-z ]", "",re.sub("\\n", "",re.sub("\s+", " ",re.sub(r'http\S+','',text.lower())))).split(" ") if i not in stopwords]))).values.astype(str)

    y = df.cyberbullying_type != "not_cyberbullying"

    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.4)
    x_val, x_test, y_val, y_test = train_test_split(x_val, y_val, test_size=0.25)

    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=2000, oov_token="<OOV>")
    tokenizer.fit_on_texts(x)
    word_index = tokenizer.word_index

    x_test = [comment]

    x_test = pad_sequences(tokenizer.texts_to_sequences(x_test), maxlen=100, padding='post', truncating='post')

    y_pred = model.predict(x_test).round().T[0]

    print(y_pred[0])

    if y_pred[0] == 0.0:
        b = "Not Bullying"
        qry1="insert into comment values(null,'%s','%s','%s','normal',curdate())"%(login_id,id,comment)
        res=insert(qry1)
        if res:
            data['status']="success"
        print(b)
    else:
        b = "Bullying Words"
        qry="insert into comment values(null,'%s','%s','%s','bullying',curdate())"%(login_id,id,comment)
        res1=insert(qry)
        if res1:
            data['status']="bullying"
        print(b,"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    qry2="SELECT COUNT(*) as cc FROM COMMENT  WHERE TYPE = 'bullying' AND login_id = '%s'"%(login_id)
    res2=select(qry2)
    aa=res2[0]['cc']
    print(login_id,"///////////////'''''///////////////////////")
    if aa<=3:
        print(res2)

        # print(cmm,"////////////////////////////////////////////")
        # if comment==b:
        #     qry="insert into comment values(null,'%s','%s','%s','bullying')"%(id,comment,user_id)
        #     res1=insert(qry)
        #     if res1:
        #         data['status']="bullying"

                
        # else:    
        #     qry1="insert into comment values(null,'%s','%s','%s','normal')"%(id,comment,user_id)
        #     res=insert(qry1)
        #     if res:
        #         data['status']="success"
    else:
        
        
        # qry3="UPDATE login INNER JOIN USER ON login.login_id=user.login_id SET login.usertype='blocked' WHERE user.user_id='%s'"%(user_id)
        # print(qry3)

        # update(qry3)
        qry3="update login set user_type='blocked' where login_id='%s'"%(login_id)
        res2=update(qry3)
        if res2:
            data['status']="failed"
        
    data['method']="comment"
    
    
    return str(data)



@api.route('/commentcount')
def commentcount():
    data={}
    id=request.args['id']
    qry="select count(*) as cc from comment where type='bullying' and login_id='%s'"%(id)
    res=select(qry)
    aa=res[0]['cc']
    if res:
        data['status']="success"
        data['data']=aa
    data['method']="commentcount"
    return str(data)



@api.route('/recentchat')
def recentchat():
    data={}
    
    id=request.args['id']
    
    # q="SELECT * FROM user INNER JOIN chat ON user.user_id = chat.sender_id group by user.fname where user.user_id='%s'"%(id)
    # q="SELECT user.*, COUNT(chat.chat_id) AS chat_count FROM USER inner JOIN chat ON user.user_id = chat.receiver_id WHERE user.user_id = '%s' GROUP BY user.user_id, user.fname"%(id)

    
    # q="SELECT chat.*, user.user_id FROM chat INNER JOIN USER ON chat.sender_id = user.user_id WHERE (chat.sender_id = '%s') ORDER BY chat.time"%(id)
    # q="SELECT chat.*, user.* FROM chat INNER JOIN user ON chat.receiver_id = user.user_id  o  chat.sender_id = user.user_id WHERE chat.sender_id='%s' or chat.receiver_id='%s' GROUP BY sender_id,receiver_id  ORDER BY chat.time"%(id,id)
    # q="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY time"%(id,id,id,id)
    # q="SELECT chat.*, user.* FROM chat INNER JOIN user ON (chat.sender_id = user.user_id OR chat.receiver_id = user.user_id) WHERE chat.sender_id = '%s' AND chat.receiver_id = '%s' UNION SELECT chat.*, user.* FROM chat INNER JOIN user ON (chat.sender_id = user.user_id OR chat.receiver_id = user.user_id) WHERE chat.sender_id = '%s' AND cORDER BY chat.time"%(id,id,id,id)


    
    # q="SELECT chat.*, user.* FROM chat INNER JOIN USER ON (chat.receiver_id = user.user_id OR chat.sender_id = user.user_id) WHERE chat.sender_id ='%s' OR chat.receiver_id ='%s' GROUP BY chat.sender_id, chat.receiver_id ORDER BY chat.time"%(id,id)
    
    
    # q="SELECT  chat.receiver_id FROM chat INNER JOIN USER ON (chat.sender_id = user.user_id OR chat.receiver_id = user.user_id) WHERE (chat.sender_id = '%s' OR chat.receiver_id = '%s') AND chat.chat_id != '%s'"%(id,id,id)
    
    q="SELECT user.* FROM USER WHERE user.login_id IN (SELECT DISTINCT chat.sender_id FROM chat WHERE chat.receiver_id = '%s' UNION SELECT DISTINCT chat.receiver_id FROM chat WHERE chat.sender_id = '%s')"%(id,id)


    res=select(q)
    
    print(res,"/////////////////////////////////////////////////")
    if res:
        data['status']="success"
        data['data']=res
    return str(data)



@api.route('/recentchatnew')
def recentchatnew():
    data={}
    sender_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']
    message=request.args['chat']
    
    qry="insert into chat values(null,'%s','user','%s','user','%s',curdate(),curtime())"%(sender_id,receiver_id,message)
    res=insert(qry)
    if res:
        data['status']="success"
    data['method']="done"
    return str(data) 



@api.route('/viewchatrecent')
def viewchatrecent():
    user_id=request.args['sender_id']
    print(type(user_id))
    receiver_id=request.args['receiver_id']

    
    data={}


    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date and time "%(user_id,receiver_id,receiver_id,user_id)
    rg=select(f)
    if rg:
       
        data['status']="success"
        data['data']=rg
        data['method']="view"

    
    

    return str(data) 



@api.route('/accountrecovery')
def accountrecovery():
    data={}
    password=request.args['password']


    qry="select * from login inner join user using(login_id) where user_name='%s' and password='%s'"%(password,password)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)


@api.route('/accountrecovery1')
def accountrecovery1():
    data={}
    newpass=request.args['newpass']
    confirmpass=request.args['confirmpass']
    id=request.args['id']
    if newpass==confirmpass:
        qry="update login set password='%s' where login_id='%s'"%(confirmpass,id)
        res=update(qry)
        if res:
            data['status']="success"
    else:
        data['status']="failed"
    return str(data)



@api.route("/warning",methods=['post','get'])
def warning():
    data={}
    id=request.args['user_id']
    qry="SELECT COUNT(*) as cc FROM COMMENT WHERE TYPE = 'bullying' AND login_id = '%s';"%(id)
    res=select(qry)
    

    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="notcount"
    return str(data)




@api.route("/count",methods=['post','get'])
def count():
    data={}
    qry="SELECT COUNT(*) as cc FROM notification where date_time=curdate() "
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="not"
    return str(data)






