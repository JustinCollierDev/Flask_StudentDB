from flask import Flask, request, jsonify, render_template
from db_config import get_db_connection # This is our database connection package/function

app = Flask(__name__)

# Landing Page (/)
@app.route('/')
def home():
    return render_template('index.html')

# CRUD : Student Page




# Running our Flask App
if __name__ == '__main__':
    app.run(debug=True)
