# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:52:53 2018

@author: itikr
"""
from flask import Flask, render_template
from forms import RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '342b34543b4554934'

posts = [{'user':'alysa','lang':'python','date':'nov 6,2018'},
       {'user':'alex','lang':'java','date':'nov 7,2018'}]
@app.route("/")
def hello():
    return render_template("mainpage.html",posts = posts)

@app.route("/register")  
def register():
    form = RegistrationForm()
    return render_template("register.html",form = form)

if __name__ == '__main__':
    app.run(debug = True,use_reloader=False)


