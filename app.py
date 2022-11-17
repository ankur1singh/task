from flask import Flask, redirect,render_template,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm

import os

#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'b\xec.\xf7}\n\x98\xf1\x0e\x0fs\xdb\xad\xc1e\xda\x1f\xa1\xe3m\xf5\xb1`\x91X'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess' 


app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://sammy:password@localhost/db_name1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(300),nullable=False)
    

    def __repr__(self) -> str:
        return f"{self.username} - {self.password}"


 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('index.html')  

@app.route('/ankur') #decorator drfines the   
def ankur():  
    return "hello, this is our Ankur SIr ji";  


@app.route('/index1')
def index1():
    user = {'username': 'Ankur'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index1.html', title='Home', user=user,posts=posts)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
       
        return redirect('/index1')
        
    return render_template('login.html', title='Sign In', form=form)

if __name__ =='__main__':  
    app.run(debug = True,port=8000) 

     