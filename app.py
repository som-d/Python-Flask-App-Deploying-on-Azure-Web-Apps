from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Azure Web Apps! le me check.'

if __name__ == '__main__':
    app.run(debug=True)