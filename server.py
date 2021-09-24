from flask import Flask

app = Flask(__name__)


# The route is used to bind a function to a URL
# The route maps a url to some logic (also known as "view function")
@app.route("/")
# A single function can be associated with multiple routes
# @app.route("/home")
# @app.route("/index")
def home():
    return "<h1>Hello World!</h1>" \
           "<p>This is going to be fun!</p>" \
           "<p>Check out the <a href='/about-us'>About Us</a> page.</p>" \
           "<p>Here's the <a href='/contact-us'>Contact Us</a> page.</p>"


@app.route("/about-us")
def about():
    return "<h1>About Us</h1>" \
           "<p>Stuff about us goes here...</p><p><a href='/'>Home Page</a></p>"


@app.route("/contact-us")
def contact():
    return "<h1>Contact Us</h1>" \
           "<p>Get in touch with us...</p><p><a href='/'>Home Page</a></p>"


if __name__ == "__main__":
    app.run(debug=True)  # setting debug=True will auto-reload the server when a file is changed
