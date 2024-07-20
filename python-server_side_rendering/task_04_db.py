from flask import Flask, render_template, request, abort
import sqlite3
import csv
import json

app = Flask(__name__)

# Function to read data from SQLite database
def fetch_from_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to read data from JSON file
def fetch_from_json():
    with open('data.json', 'r') as file:
        return json.load(file)

# Function to read data from CSV file
def fetch_from_csv():
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

@app.route('/products')
def display_products():
    source = request.args.get('source')
    
    if source == 'json':
        data = fetch_from_json()
    elif source == 'csv':
        data = fetch_from_csv()
    elif source == 'sql':
        data = fetch_from_sqlite()
        data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in data]
    else:
        return "Wrong source", 400
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
