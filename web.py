from flask import Flask
app = Flask(__name__)



@app.route('/' ,  methods=["GET"])
def hello():
    return "Hello World! this is the first step of Kremlin web!"

if __name__ == '__main__':
    app.run()