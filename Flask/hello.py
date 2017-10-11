from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('success')
def success():
    return render_template('success')





app.run(debug=True)
