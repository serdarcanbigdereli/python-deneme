from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Web App with Python Flask!'

application.run(host='0.0.0.0', port=80)