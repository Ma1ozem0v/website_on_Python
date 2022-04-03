from flask import Flask

app = Flask(__name__)


@app.route('/')
def base():
    with open('templates/base.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/maths')
def maths():
    with open('templates/maths.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/physics')
def physics():
    with open('templates/physics.html', 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
