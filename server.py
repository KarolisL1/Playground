from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play') #just to test
def hello_world():
    return render_template('index.html', x=3, color="blue")

@app.route('/play/<int:x>') #just to test
def hello_world2(x):
    return render_template('index.html', x=x, color="blue")

@app.route('/play/<int:x>/<color>') #just to test
def hello_world3(x, color):
    return render_template('index.html', x=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
