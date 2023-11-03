from flask import Flask, request, jsonify
import json
import db

with open('items.json', 'r') as items_file:
        items = json.load(items_file)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_items():
    search = request.args.get('search')
    print(search)
    items = db.find_items(search)
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True, port=8000)