from flask import Flask, request, redirect
import persist
import loader

app = Flask(__name__)

def get_raw(path):
    t = open('./static/'+path)
    x = t.read()
    t.close()
    return x

@app.route('/')
@app.route('/index.html')
def welcome():
    return get_raw('index.html')

@app.route('/login.html')
def login():
    return get_raw('login.html')

@app.route('/submit')
def generate():
    if request.method == 'GET':
        ret = persist.courses_from_ehall(
            request.args['id'],
            request.args['password'],
            force=('force' in request.args and request.args['force'] == '1')
        )
        if ret is False:
            return '用户名或密码错误'
        return redirect('/export/'+ret)


@app.route('/export/<uuid>')
def export(uuid):
    return str(loader.load(uuid))

if __name__ == '__main__':
    app.run('0.0.0.0', 1234)
