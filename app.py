from flask import Flask
import mysql.connector

app = Flask(__name__)

# RDS connection details
db = mysql.connector.connect(
    host="terraform-20250629134551565100000001.clk8aykca23k.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Password123!",
    database="flaskdb"
)

@app.route("/")
def home():
    return "✅ Hello from Flask behind ALB!"

@app.route("/db")
def db_check():
    cursor = db.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone()
    return f"✅ Connected to RDS! Time: {result[0]}"
