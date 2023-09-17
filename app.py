from flask import Flask, render_template, jsonify
import main

app = Flask(__name__)

fileCounter = 2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_car_count')
def get_number():
    global fileCounter
    carCount = main.predictCarCount(fileCounter)
    if fileCounter < 43:
        fileCounter += 1
    else:
        fileCounter = 2
    return jsonify({'number': carCount})

if __name__ == '__main__':
    app.run(debug=True)
