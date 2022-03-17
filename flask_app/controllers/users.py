from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template("index.html")

'''READ'''
# read all
@app.route("/read")
def read():
    select_all = User.select_all()
    # returns a list of classes
    return render_template("output.html", output = select_all)

@app.route("/read_one/<int:id>")
def read_one(id):
    data={'id':id}
    result=User.get_one(data)
    return render_template("output_one.html", output = result)

'''CREATE'''
@app.route("/create")
def new():
    return render_template("create.html")

@app.route('/create_new', methods=["POST"])
def create():
    data ={k:v for k,v in request.form.items()}
    print(data)
    # {'first_name': 'x', 'last_name': 'x', 'email': 'x', 'password': 'x'}
    # creates a dictionary with the form names and values
    new_user=User.insert(data)
    # save the new user incase you want to use it later
    return redirect('/read')


'''UPDATE'''
@app.route('/edit/<int:id>')
def show(id):
    data ={ 
    # get data from url variable
        "id":id
        #insert as id
    }
    output=User.get_one(data)
    # use the get_one fucntion in the User class
    # save to pass to html page
    return render_template("edit.html", output=output)

@app.route('/process_edit',methods=["POST"])
def process_edit():
    data={k:v for k,v in request.form.items()}
    User.update(data)
    # from the user class, use the update method, 
    # pass in arg of data from request.form
    return redirect('/read')


'''DELETE'''
@app.route("/delete/<int:id>")
def delete(id):
    data={'id':id}
    print(data)
    User.delete(data)
    return redirect('/read')

@app.route('/', defaults={"path":""})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("catchall.html")