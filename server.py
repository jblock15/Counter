from flask import Flask, render_template, flash, request, redirect, session
app = Flask(__name__)
app.secret_key = "Effyousecretkey"

@app.route ('/')
def index():
    if 'num' not in session:
        session["num"] = 0
    else:
        session["num"] += 1
    return render_template('index.html')


@app.route ('/plus')
def add_two():
    session['num'] += 1
    return redirect('/')

@app.route ('/clear')
def reset():
    session['num'] = 0
    session.clear()
    return redirect('/')

app.run(debug=True)
