from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
SETTINGS_FILE = 'settings.json'

# Default schedule (copied from your HTML)
DEFAULT_SCHEDULE = {
    "0": [
    ],
    "1": [
    ],
    "2": [
    ],
    "3": [
    ],
    "4": [
    ],
    "5": [
    ],
    "6": [
    ]
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Create default settings
        default = {
            "schedule": DEFAULT_SCHEDULE,
            "gridMode": "vertical"
        }
        save_settings(default)
        return default

def save_settings(data):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    return jsonify(load_settings())

@app.route('/api/schedule', methods=['POST'])
def update_schedule():
    data = request.get_json()
    save_settings(data)
    return jsonify({"status": "ok"})