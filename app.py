from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append(task)
        return jsonify({'tasks': tasks})
    return jsonify({'error': 'Task cannot be empty'}), 400

@app.route('/remove', methods=['POST'])
def remove_task():
    task = request.json.get('task')
    if task in tasks:
        tasks.remove(task)
        return jsonify({'tasks': tasks})
    return jsonify({'error': 'Task not found'}), 404

@app.route('/clear', methods=['POST'])
def clear_tasks():
    tasks.clear()
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)

