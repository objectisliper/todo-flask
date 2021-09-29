from flask import Flask, render_template, request, redirect

from models import Note
from utils import session_scope

app = Flask(__name__)


@app.route('/')
def tasks_list():
    with session_scope() as session:
        notes = session.query(Note).all()
        return render_template('list.html', notes=notes)


@app.route('/task', methods=['POST'])
def add_task():
    with session_scope() as session:
        content = request.form
        if not content:
            return 'Error'

        note = Note(name=content['name'], description=content['description'])
        session.add(note)
        return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with session_scope() as session:
        note = session.query(Note).filter_by(id=task_id).first()
        if not note:
            return redirect('/')

        session.delete(note)
        return redirect('/')


if __name__ == '__main__':
    app.run()
