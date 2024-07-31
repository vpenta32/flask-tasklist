from app.models import *

def addEvent(db, form):
    newEvent = Event(title=form.title.data, description=form.description.data, user_id=form.user_id.data, date=form.date.data)
    db.session.add(newEvent)
    db.session.commit()

def getEvents(db, user, date):
    user_id = user.id
    events = Event.query.filter_by(user_id=user_id, date=date)
    return events