from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'



@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        return render_template ('index.html')
    else:
        session['count'] += 1
        return render_template ('index.html')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect ('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect ('/')


if __name__=="__main__":
    app.run(debug=True)