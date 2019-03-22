from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, send_from_directory, make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database import Base, City, Immobile, User, engine
from flask import session as login_session
import httplib2
import os
import sys
import codecs
from flask_httpauth import HTTPBasicAuth
from flask_bootstrap import Bootstrap
import string
import requests

auth = HTTPBasicAuth()
app = Flask(__name__)
Bootstrap(app)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/city/new/', methods=['GET', 'POST'])
def newCity():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newcity = City(name=request.form['name'],
                       user_id=login_session['user_id'])
        session.add(newcity)
        session.commit()
        flash('New City %s Successfully Created' % newcity.name)
        return redirect(url_for('showCities'))
    else:
        return render_template('newCity.html')
    # return "This page creates a new city"


@app.route('/city/<int:city_id>/edit/', methods=['GET', 'POST'])
def editCity(city_id):
    editedCity = session.query(City).filter_by(id=city_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedCity.user_id != login_session['user_id']:
        print "\ncity.user_id: %s\n" % editedCity.user_id
        return "<script> function myFunction(){alert('You are not authorized to edit this City. Please create your own city in order to edit.');}</script> <body onload='myFunction()' > "
    if request.method == 'POST':
        if request.form['name']:
            editedCity.name = request.form['name']
            flash('City Successfully Edited %s' % editedCity.name)
            return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('editedcity.html', city=editedCity)
    # return "This page edit the selected city"


@app.route('/city/<int:city_id>/delete/', methods=['GET', 'POST'])
def deleteCity(city_id):
    cityDelete = session.query(City).filter_by(id=city_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if cityDelete.user_id != login_session['user_id']:
        print "\ncity.user_id: %s\n" % cityDelete.user_id
        print "login_session['user_id'] %s" % login_session['user_id']
        return "<script> function myFunction(){alert('You are not authorized to delete this City. Please create your own city in order to delete.');}</script> <body onload='myFunction()' > "
    if request.method == 'POST':
        session.delete(cityDelete)
        session.commit()
        flash('%s Successfully Deleted' % cityDelete.name)
        return redirect(url_for('showCities'))
    else:
        return render_template('deleteCity.html', city=cityDelete)
    # return "This page deletes the selected city"

@app.route('/city/<int:city_id>/immobile/new/', methods=['GET', 'POST'])
def newImmobile(city_id):
    if 'username' not in login_session:
        return redirect('/login')
    city = session.query(City).filter_by(id=city_id).one()
    # if login_session['user_id'] != city.user_id:
    # return "<script>function myFunction() {alert('You are not authorized to
    # add immobiles to this city. Please create your own city in order to add
    # immobiles.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        newImm = Immobile(address=request.form['address'],
                          description=request.form['description'],
                          squarefeet=request.form['squarefeet'],
                          bedrooms=request.form['bedrooms'],
                          bathrooms=request.form['bathrooms'],
                          city_id=city_id,
                          user_id=login_session['user_id'])
        session.add(newImm)
        session.commit()
        flash('New Immobile Successfully Created')
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('newimmobile.html', city_id=city_id)
    # return "This page creates a new immobile to the specified city"


@app.route('/city/<int:city_id>/immobile/<int:immobile_id>/edit',
           methods=['GET', 'POST'])
def editImmobile(city_id, immobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedImmobile = session.query(Immobile).filter_by(id=immobile_id).one()
    city = session.query(City).filter_by(id=city_id).one()
    if login_session['user_id'] != editedImmobile.user_id:
        print "\neditedImmobile.user_id: %s\n" % editedImmobile.user_id
        print "login_session['user_id']: %s" % login_session['user_id']
        return "'<script> function myFunction(){alert('You are not authorized to create immobiles to this city. Please create your own city in order to edit immobiles.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['address']:
            editedImmobile.address = request.form['address']
        if request.form['description']:
            editedImmobile.description = request.form['description']
        if request.form['squarefeet']:
            editedImmobile.squarefeet = request.form['squarefeet']
        if request.form['bedrooms']:
            editedImmobile.bedrooms = request.form['bedrooms']
        if request.form['bathrooms']:
            editedImmobile.bathrooms = request.form['bathrooms']
        session.add(editedImmobile)
        session.commit()
        flash('Immobile Successfully Edited')
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('editedimmobile.html', city_id=city_id,
                               immobile_id=immobile_id, item=editedImmobile)
    # return "This page edits a certain immobile of the selected city"


@app.route('/city/<int:city_id>/immobile/<int:immobile_id>/delete',
           methods=['GET', 'POST'])
def deleteImmobile(city_id, immobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    city = session.query(City).filter_by(id=city_id).one()
    deletedimmobile = session.query(Immobile).filter_by(id=immobile_id).one()
    if login_session['user_id'] != deletedimmobile.user_id:
        return "'<script> function myFunction(){alert('You are not authorized todelete immobiles to this city. Please create your own city in order to delete items.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(deletedimmobile)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('deletedimmobile.html', city_id=city_id,
                               item=deletedimmobile)
    # return "This page deletes a certain immobile of the selected city"
