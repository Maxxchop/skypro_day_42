from flask import render_template, Flask

app = Flask(__name__)

# Первое задание
@app.route('/users/<id>')
def users(id):
    return render_template(
        'users/show.html',
        id=id,
    )

