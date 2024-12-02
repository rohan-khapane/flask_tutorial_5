from flask import Flask ,Blueprint,request,render_template,session

bp=Blueprint("session",__name__)

@bp.route('/sess/')
def sess():
    session['name']='paarth'
    # session['age']=25
    session['address']='panvel'
    return render_template("session/session.html",message='session data')

@bp.route('/sess/set_data/')
def set_data():
    # session['name']='paarth'
    # session['age']=25
    return render_template("session/set_data.html",message='session data set')
    #return render_template("session/set_data.html",message=f"{session['name']} and {session['age']}")

@bp.route('/sess/get_data/')
def get_data():
    if('name' in session and 'age' in session): 
        name=session['name']
        age=session['age']
        add=session['address']
        
        return render_template('session/get_data.html',message=f"name is :{name} and age is :{age} and address is: {add}")
    else:
        return "no data present in session"