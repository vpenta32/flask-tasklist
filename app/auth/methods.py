from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash

def addUser(db, form):
    hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
    newUser = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(newUser)
    db.session.commit()

def emailExists(db, form):
    email = form.email.data
    return User.query.filter_by(email=email).first() is not None

def autenticateUser(db, form):
    if emailExists(db, form):
        email = form.email.data
        inputPassword = form.password.data
        
        user = User.query.filter_by(email=email).first()
        hashed_password = user.password
        if check_password_hash(hashed_password, inputPassword):
            return user
        else:
            return None
    else:
        return None