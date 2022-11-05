from flask import render_template, Flask, request

app = Flask(__name__)

# Второе задание
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/users')
def users_search():
    query = request.args.get('query')
    if not query:
        query = ''
    filtered_users = [i for i in users if query in i]
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=query,
    )

