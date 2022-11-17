from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b\xec.\xf7}\n\x98\xf1\x0e\x0fs\xdb\xad\xc1e\xda\x1f\xa1\xe3m\xf5\xb1`\x91X'

app = Flask(__name__) #creating the Flask class object 
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///ankur.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created= db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('index.html')  

@app.route('/ankur') #decorator drfines the   
def ankur():  
    return "hello, this is our Ankur SIr ji";  


@app.route('/index')
def index():
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
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ =='__main__':  
    app.run(debug = True,port=8000) 