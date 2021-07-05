from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'

from flask import request, redirect

from flask import render_template


@app.route('/me', methods=['GET'])
def message():
    return render_template("me.html")

@app.route('/contact', methods=['GET', 'POST'])
def message1():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")