#import statements go here
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, StringField, SubmitField
from wtforms.validators import Required, Email ##add separate validators

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

@app.route('/')
def home():
    return "Hello, world!"

class iTunesForm(FlaskForm): #inherits a parameter from flask form
    artist = StringField('enter an artist', validators=[Required() ]) #input types, labels, required validators
    numresult = IntegerField('enter a number of results', validators=[Required() ])
    email = StringField('enter an email address', validators=[Required(), Email()])
    submit = SubmitField('Submit') #creates submit button


@app.route('/itunes-form')
def itunes_form():
    #what code goes here?
    itunes_form = iTunesForm() #create itunes-form.html
    return render_template('itunes-form.html', form=itunes_form) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
    #what code goes here?
    form = iTunesForm(request.form)
    params = {}
    if request.method == 'POST' and form.validate_on_submit():
        params['term'] = form.artist.data
        params['limit'] = form.apires.data
        response = requests.get('https://itunes.apple.com/search?', params = params)
        response_text = json.loads['results']
        result_py = response_text['results']

        return render_template('itunes-results.html', result_html = result_py)

    flash('All fields are required!')
    return redirect(url_for('itunes_form')) #this redirects you to itunes_form if there are errors

if __name__ == '__main__':
    app.run()
