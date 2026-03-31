from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_feedback, get_all_feedback

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    feedback = get_all_feedback()
    return render_template('index.html', feedback=feedback)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')

    if name and message:
        insert_feedback(name, message)

    return redirect(url_for('index'))

@app.route('/feedback')
def feedback_page():
    feedback = get_all_feedback()
    return render_template('feedback.html', feedback=feedback)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)