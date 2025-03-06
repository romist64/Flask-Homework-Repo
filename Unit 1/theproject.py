from flask import Flask, render_template, request

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

@app.route('/results', methods=['POST'])
def results():
   color = request.form['color']
   luck_num = request.form['luck_num']
   fav_class = request.form['fav_class']
   best_pix = request.form['best_pix']
   return render_template("results.html", color=color, luck_num=luck_num, fav_class=fav_class, best_pix=best_pix)

if __name__ == '__main__':
   app.run()