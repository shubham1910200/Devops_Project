from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks (for demo purposes)
tasks = []

# Home route to display the tasks and form
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')  # Get task from form input
    if task:
        tasks.append(task)  # Add task to the list
    return redirect(url_for('index'))  # Redirect back to home

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  # Remove task by index
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
