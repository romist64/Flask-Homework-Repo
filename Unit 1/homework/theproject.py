from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask! <a href='/Two'>Goodbye!</a><br><a href='/form'>Form</a>"
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
   best_pix = request.form['best_pix'].lower().strip()
   films = ["toy story","a bug's life","toy story 2","monsters, inc.",
      "finding nemo", "the incredibles","cars","ratatouille","wall-e","up",
      "toy story 3","cars 2", "brave","monsters university","inside out",
      "the good dinosaur","finding dory", "cars 3","coco","incredibles 2",
      "toy story 4","onward","soul"]
   if best_pix not in films:
      best_pix = "Sorry, '{0}' is not a Pixar film.".format(best_pix.title())
   return render_template("results.html", color=color, luck_num=luck_num, fav_class=fav_class, best_pix=best_pix)

if __name__ == '__main__':
   app.run()