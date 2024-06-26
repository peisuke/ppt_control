from flask import Flask, jsonify, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/next', methods=['POST'])
def receive_data():
    pyautogui.click()
    return jsonify({"result": "OK"})

@app.route('/api/back', methods=['POST'])
def receive_back():
    pyautogui.press('left')
    return jsonify({"result": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
