from flask import Flask,request,redirect
from flask.templating import render_template
from flask_migrate import migrate,Migrate
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
migrate=Migrate(app,db)
class Participants(db.Model):
    Id=db.Column(db.Integer,unique=True,primary_key=True)
    name=db.Column(db.String(20),unique=False,nullable=False)
    institute=db.Column(db.String(30),unique=False,nullable=True)
    phone=db.Column(db.String(10),unique=False,nullable=False)
    email=db.Column(db.String(15),unique=False,nullable=False)
    applied=db.Column(db.String(35),unique=False,nullable=False)
    def __repr__(self):
        return f"Id:{self.Id},name:{self.name},institute:{self.institute},phone:{self.phone},email:{self.email},applied:{self.applied}"
@app.route('/')
def my_index():
    events=[{'name':'Mock Mun','date':'28 January, 2024','time':'10AM-5PM','desc':'For all those newly starting MUNers who want to have the experience of an actual MUN conference, this is a great chance.'},{'name':'Annual Conference','date':'14,15,16 February, 2024','time':'10AM-5PM','desc':'The most awaited Annual Conference of NITSMUN gives the participants a chance to test their own skills. Join us to make this event a great success.'}]
    fields=[{'name':'name','type':'text'},{'name':'institute','type':'text'},{'name':'phone','type':'text'},{'name':'email','type':'email'}]
    return render_template('index.html',events=events,fields=fields)
@app.route('/applied',methods=['POST'])
def applied():
    name=request.form.get('name')
    institute=request.form.get('institute')
    phone=request.form.get('phone')
    email=request.form.get('email')
    applied=request.form.get('applied')
    if(name!='' and institute!='' and phone!='' and email!='' and applied!=''):
        Participant=Participants(name=name,institute=institute,phone=phone,email=email,applied=applied)
        db.session.add(Participant)
        db.session.commit()
        return "Registered Successfully!! You may exit this page"
    else:
        return redirect('/')
if(__name__=='__main__'):
    app.run(debug=True,host='0.0.0.0')