from flask import Flask, request, render_template, jsonify
import sqlite3
import json
import csv

app = Flask(__name__)

def fetch_data_from_json():
    with open('products.json') as f:
        return json.load(f)

def fetch_data_from_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def fetch_data_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    
    if source == 'json':
        data = fetch_data_from_json()
    elif source == 'csv':
        data = fetch_data_from_csv()
    elif source == 'sql':
        data = fetch_data_from_sql()
    else:
        return "Wrong source", 400
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
