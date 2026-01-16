from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
#Oh wait the square brackets don't display
def home():
    return "The server is working! Go to /login for the form. <br> You can also go to /user/[name]"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}!'
app.add_url_rule('/user/<username>','show_user',show_user)
#ok well honestly I don't know how this changes anything

@app.route("/hello")
def hello():
    return "Hello, I hope this works"

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the ID {id}'

if __name__ == '__main__':
    app.run(port=8010, debug=True, use_reloader=False)
    
    
