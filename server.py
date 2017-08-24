from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "sosecret"

@app.route('/')
def index():
	return render_template("index.html")



@app.route('/ninjas/')
def ninjas():
	count=0
	return render_template('ninjas.html', count=count)


@app.route('/ninjas/<vararg>')


def ninja(vararg):
    count=len(vararg)
    if vararg == 'red':
        return render_template("ninjas.html", vararg=vararg, count=count)
    elif vararg == 'orange':
        return render_template("ninjas.html", vararg=vararg, count=count)
    elif vararg == 'blue':
        return render_template("ninjas.html", vararg=vararg, count=count)
    elif vararg == 'purple':
        return render_template("ninjas.html", vararg=vararg, count=count)
    else:
        return render_template("ninjas.html", vararg=vararg, count=count)
app.run(debug=True)
