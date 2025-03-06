from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask! <a href='/Two'>Goodbye!</a>"
   return message

@app.route('/Two')
def the():
   message = "The Second: The First"
   return message

@app.route('/form')
def form():
   return render_template("form.html")

if __name__ == '__main__':
   app.run()