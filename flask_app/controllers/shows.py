from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_app.models.like import Like


@app.route('/new/show')
def show():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id':session['user_id']
    }
    return render_template('show.html',user=User.get_by_id(data))

@app.route('/create/new_show',methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/new/show')
    data={
        'title':request.form['title'],
        'network':request.form['network'],
        'release_date':request.form['release_date'],
        'type':request.form['type'],
        'age_limit':request.form['age_limit'],
        'description':request.form['description'],
        'user_id':session['user_id']
    }
    Show.save(data)
    return redirect('/home')

@app.route('/edit/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id':id
    }
    user_data={
        'id':session['user_id']
    }
    return render_template('edit_show.html',edit=Show.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/show',methods=['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect(f"/edit/show/{request.form['id']}")
    data={
        'title':request.form['title'],
        'network':request.form['network'],
        'release_date':request.form['release_date'],
        'type':request.form['type'],
        'age_limit':request.form['age_limit'],
        'description':request.form['description'],
        'id':request.form['id']
    }
    Show.update(data)
    return redirect('/home')

@app.route('/delete/show/<int:id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id':id
    }
    
    Show.delete(data)
    return redirect('/home')

@app.route('/show/<int:id>')
def s(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id':id
    }
    user_data={
        'id':session['user_id']
    }
    d = {
        'show_id':id
    }
    return render_template('show_view.html',show=Show.get_one(data),user=User.get_by_id(user_data),users=User.get_all(),likes=Like.get_likes_count(d))


@app.route ('/like/show/<int:id>' ,methods=["POST"])
def like_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'user_id':session['user_id'],
        'show_id':id
    }
    Like.create_like(data)
    return redirect('/home')

@app.route ('/like/delete/<int:id>' ,methods=["POST"])
def unlike_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'user_id':session['user_id'],
        'show_id':id
    }
    Like.delete_like(data)
    return redirect('/home')