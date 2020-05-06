from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello!!!\n'

if __name__ == "__main__":
    app.run('0.0.0.0', port=9000, debug=False)