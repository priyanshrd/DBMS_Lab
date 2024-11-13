import mysql.connector
from flask import Flask, request, jsonify
from flask import render_template
app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',         # Replace with your MySQL username
    'password': 'root@123',     # Replace with your MySQL password
    'database': 'insurance_db'       # Replace with your database name
}

@app.route("/add-accident-page", methods=["GET"])
def add_accident_page():
    return render_template("add_accident.html")

# Route to render the get reports page
@app.route("/get-reports-page", methods=["GET"])
def get_reports_page():
    return render_template("get_reports.html")

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Endpoint to add a new accident
@app.route("/http://127.0.0.1:5000/add-accident", methods=["POST"])
def add_accident():
    data = request.get_json()
    report_number = data["report_number"]
    date = data["date"]
    location = data["location"]

    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert data into ACCIDENT table
    query = "INSERT INTO ACCIDENT (report_number, date, location) VALUES (%s, %s, %s)"
    cursor.execute(query, (report_number, date, location))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 201

# Endpoint to get accident reports
@app.route("/http://127.0.0.1:5000/get-reports", methods=["GET"])
def get_reports():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch accident data
    query = "SELECT report_number, date, location FROM ACCIDENT"
    cursor.execute(query)
    reports = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert to list of dictionaries
    report_list = [{"report_number": r[0], "date": r[1], "location": r[2]} for r in reports]
    return jsonify(report_list)

if __name__ == "__main__":
    app.run(debug=True)
