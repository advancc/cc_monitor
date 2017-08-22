from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import requests

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    #url="http://127.0.0.1:3000/render/dashboard-solo/db/yong-hu-zu-jian-kong-ping-tai?orgId=1&panelId=9&from=1499103357866&to=1500109434678&var-vacctgroup=physics&theme=light&width=1000&height=500&tz=UTC%2B08%3A00"
    #img=requests.get(url)
    return render_template('index.html',
                           current_time=datetime.utcnow())


#@app.route('/user/<name>')
#def user(name):
#    return render_template('user.html', name=name)



if __name__ == '__main__':
    manager.run()
