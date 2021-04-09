from flask import Flask, render_template


# Takes the name from the current module and creates an argument (__name__). The route() function of the Flask class is a decorator, 
# which tells the application which URL should call the associated function. app.route(rule, options)
application = Flask(__name__)


@application.route("/")
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    application.run()
