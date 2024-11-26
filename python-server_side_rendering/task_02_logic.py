#!/usr/bin/python3
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Items Page! Visit /items to see the list."

@app.route('/items')
def items():
    try:
        with open('items.json') as file:
            data = json.load(file)
        return render_template('items.html', items=data.get('items', []))
    except FileNotFoundError:
        return "Error: items.json file not found.", 404
    except json.JSONDecodeError:
        return "Error: Failed to parse items.json.", 500

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
