from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[InputRequired()])
    date = DateField('Task Date', format='%Y-%m-%d', validators=[InputRequired()])

tasks = [
    {"id": 1, "title": "Event 1", "start": "2023-11-15"},
    {"id": 2, "title": "Event 2", "start": "2023-11-18"}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    form = TaskForm(request.form)
    if form.validate():
        task = {
            "id": len(tasks) + 1,
            "title": form.name.data,
            "start": form.date.data.strftime('%Y-%m-%d')
        }
        tasks.append(task)
        return jsonify({"success": True, "message": "Task added successfully"})
    else:
        return jsonify({"success": False, "errors": form.errors})

if __name__ == '__main__':
    app.run(debug=True)
