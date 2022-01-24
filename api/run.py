# from flask import Flask
# from flask_cors import CORS
# from flask_restful import Api
# from views import Quote

# app = Flask(__name__)
# CORS(app)
# # api = Api(app)


# # api.add_resource(Quote, '/')

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)

from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "<p>Flask here. Cool.</p>"

@app.route("/<name>")
def hello(name):
    # return f"Hey, {escape(name.capitalize())}!"
    name = escape(name.capitalize())
    return render_template('hey.html', name=name)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))    
#     print(url_for('profile', username='John Doe'))