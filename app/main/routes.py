from flask import render_template, flash, request, redirect, url_for
from . import main
from flask_login import login_required, current_user

from app.forms import *
from .methods import *

from datetime import datetime, timedelta

@main.route('/')
def index():
    return render_template('home/home.html')

@main.route('/tasklist', methods=['GET', 'POST'])
@login_required
def tasklist():
    form = AddEventForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            addEvent(db, form)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    events = getEvents(db, current_user, date.today())
    dates = [date.today()-timedelta(days=1), date.today(), date.today()+timedelta(days=1)]
    return render_template('profile/tasklist.html', user=current_user, form=form, events=events, dates=dates)

@main.route('/removeEvent/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)

    if event.user_id != current_user.id:
        flash('You are not authorized to delete this event.', 'danger')
        return redirect(url_for('main.tasklist'))
    
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('main.tasklist'))

@main.route('/doneEvent/<int:event_id>', methods=['POST'])
@login_required
def done_event(event_id):
    event = Event.query.get_or_404(event_id)

    if event.user_id != current_user.id:
        flash('You are not authorized to mark as done this event.', 'danger')
        return redirect(url_for('main.tasklist'))
    
    event.done = True
    db.session.commit()
    flash('Event marked as done successfully!', 'success')
    return redirect(url_for('main.tasklist'))

@main.route('/getByDate/<string:event_date>/<string:side>', methods=['POST'])
@login_required
def getByDate(event_date, side):
    form = AddEventForm()
    events = getEvents(db, current_user, event_date)
    date_object = datetime.strptime(event_date, '%Y-%m-%d').date()
    dates = [date_object-timedelta(days=1), date_object, date_object+timedelta(days=1)]
    return render_template('profile/tasklist.html', user=current_user, form=form, events=events, dates=dates, side=side)