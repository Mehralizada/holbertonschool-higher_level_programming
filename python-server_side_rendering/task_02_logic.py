from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Read the JSON file
    with open('items.json') as json_file:
        data = json.load(json_file)
    
    # Extract the list of items
    items_list = data.get('items', [])
    
    # Render the template with the items
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
