from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'key'


@app.route('/')
def count_user():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template("index.html",counter=session['counter'])

@app.route('/click',methods=['GET','POST'])
def add_two():
    session['counter']+=1
    return redirect('/')

@app.route('/reset',methods=['GET','POST'])
def reset_count():
    session['counter']=-1
    return redirect('/')

app.run(debug=True)
