from flask import Flask, request, render_template, redirect, url_for
from db_config import get_db_connection # This is our database connection package/function

app = Flask(__name__)

# Landing Page (/)
@app.route('/')
def index():
    return render_template('index.html')

# Navigate to Students Page (/students)
@app.route('/students')
def students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    connection.close()

    # CRUD - Students Page (/students) - GET (Read)
    # We pass in our list of Students to the render template to display them under our form
    return render_template('students.html', students=students)

# CRUD : Student Page
# Students Page (/students) - POST (CREATE)
@app.route('/students/create', methods=['POST'])
def create_student():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    amount_due = request.form['amount_due']
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO students (first_name, last_name, dob, amount_due) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, dob, amount_due)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('students'))

# Students Page (/students) - PUT (Update)
@app.route('/students/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    amount_due = request.form['amount_due']
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "UPDATE students SET first_name = %s, last_name = %s, dob = %s, amount_due = %s WHERE student_id = %s"
    values = (first_name, last_name, dob, amount_due, student_id)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('students'))

# Students Page (/students) - DELETE (DELETE)
@app.route('/students/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('students'))


# Running our Flask App
if __name__ == '__main__':
    app.run(debug=True)
