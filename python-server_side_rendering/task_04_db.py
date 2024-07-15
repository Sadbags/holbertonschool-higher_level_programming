from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['items']

def read_csv(file_path):
    items = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            items.append(row)
    return items

def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return items

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        items = read_json('products.json')
    elif source == 'csv':
        items = read_csv('products.csv')
    elif source == 'sql':
        items = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        items = [item for item in items if str(item['id']) == product_id]
        if not items:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
