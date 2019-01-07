from flask import Flask, render_template, jsonify

import RPi.GPIO as GPIO
from NCode import NCar
import atexit

atexit.register(GPIO.cleanup)

app = Flask(__name__)


# 首页
@app.route("/")
def index():
    return render_template('index.html')


# 驾驶
@app.route('/drive/<action>', methods=['GET'])
def drive(action):
    if action == 'forward':
        car.forward()
    if action == 'backOff':
        car.backOff()
    if action == 'leftTurn':
        car.leftTurn()
    if action == 'rightTurn':
        car.rightTurn()
    if action == 'stop':
        car.stop()
    return jsonify({'success': 'ok'})


# 重置
@app.route('/reset', methods=['GET'])
def reset():
    GPIO.cleanup()
    return jsonify({'success': 'ok'})


car = NCar.NCar()

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except Exception as e:
        GPIO.cleanup()
