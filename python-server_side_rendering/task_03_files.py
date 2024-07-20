from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

@app.route('/products', methods=['GET'])
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=filtered_products)
        except ValueError:
            return render_template('product_display.html', error="Invalid id")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
