from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL DB connection using env variables
db = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_NAME']
)

cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL
    )
""")
db.commit()

# -------------------------------
# HTML Interface Routes
# -------------------------------

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    new_title = request.form['title']
    cursor.execute("UPDATE tasks SET title = %s WHERE id = %s", (new_title, id))
    db.commit()
    return redirect('/')

# -------------------------------
# REST API Endpoints for Testing via curl
# -------------------------------

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify([{'id': t[0], 'title': t[1]} for t in tasks])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    db.commit()
    return jsonify({'message': 'Task created'}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    new_title = data.get('title')
    cursor.execute("UPDATE tasks SET title = %s WHERE id = %s", (new_title, id))
    db.commit()
    return jsonify({'message': 'Task updated'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()
    return jsonify({'message': 'Task deleted'})

# -------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
