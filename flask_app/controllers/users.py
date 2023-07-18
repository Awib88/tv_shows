from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_app.models.like import Like
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('log_reg.html')

@app.route('/register',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id=User.save(data)
    session['user_id'] = id
    return redirect('/home')

@app.route('/login',methods=['POST'])
def login():
    user_in_db =User.get_by_email(request.form)
    if not user_in_db:
        flash("Invalid Email",'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Password",'login')
        return redirect('/')
    session['user_id']=user_in_db.id
    return redirect('/home')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':session['user_id']
    }
    result= Like.does_user_like_show(data)
    return render_template("home.html",user=User.get_by_id(data),shows=Show.get_all_by_date(),users=User.get_all(),count=Show.count_all(),result=result)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
