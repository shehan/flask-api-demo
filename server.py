from flask import Flask
from flask_restful import Api

from student import Student, StudentList

app = Flask(__name__)
api = Api(app)


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
           "<p>Here's the <a href='/contact-us'>Contact Us</a> page.</p>" \
            "<p>Here's the <a href='/api'>API Demo</a> page.</p>"


@app.route("/about-us")
def about():
    return "<h1>About Us</h1>" \
           "<p>Stuff about us goes here...</p><p><a href='/'>Home Page</a></p>"


@app.route("/contact-us")
def contact():
    return "<h1>Contact Us</h1>" \
           "<p>Get in touch with us...</p><p><a href='/'>Home Page</a></p>"


@app.route("/api")
def api_student():
    return "<h1>REST API Example</h1>" \
           "<p><a href='/api/students' target='_blank'>View All Students</a></p>" \
           "<p><a href='/api/find-student' target='_blank'>Find A Student</a></p>" \
           "<p><a href='/api/create-student' target='_blank'>Create New Student</a></p>" \
           "<p><a href='/'>Home Page</a></p>"


@app.route("/api/create-student")
def api_create_student():
    return "<h1>REST API Example - Create New Student</h1>" \
           "<script>" \
           "function createStudent(){" \
           "var student_first_name = document.getElementsByName('first_name')[0].value;" \
           "var student_last_name = document.getElementsByName('last_name')[0].value;" \
           "var student_dob = document.getElementsByName('dob')[0].value;" \
           "var result = document.getElementsByName('result')[0];" \
           "xhr = new XMLHttpRequest();" \
           "url = '/api/students';" \
           "xhr.open('POST', url, true);" \
           "xhr.setRequestHeader('Content-Type', 'application/json');" \
           "xhr.onreadystatechange = function () {" \
           " if (xhr.readyState === 4 && xhr.status === 200) {" \
           "   result.innerHTML = this.responseText;" \
           "  }" \
           "};" \
           "var data = JSON.stringify([{'first_name':student_first_name,'last_name':student_last_name,'DoB':student_dob}]);" \
           "xhr.send(data);"\
           "}" \
           "</script>"\
           "<p> <form id='create_student_form'>" \
           "<label> First Name: <input name='first_name' type='text' required autocomplete='off'/> </label> <br><br>" \
           "<label> Last Name: <input name='last_name' type='text' required autocomplete='off'/> </label> <br><br>"\
           "<label> DoB: <input name='dob' type='date' required autocomplete='off'/> </label> <br><br>" \
           "<input type='button' value='Create' onclick='createStudent()'/></form></p>"\
            "<p name='result' style='color:green'></p>" \



@app.route("/api/find-student")
def api_find_student():
    return "<h1>REST API Example - Find A Student</h1>" \
           "<script>" \
           "function findStudent(){" \
           "var api_url = '/api/students/' + document.getElementsByName('student_id')[0].value;" \
           "var student_form = document.getElementById('find_student_form');" \
           "student_form.action = api_url;" \
           "}" \
           "</script>"\
           "<p> <form id='find_student_form' onsubmit='findStudent()'><label> Student Id: <input name='student_id' type='number' placeholder='Enter Id Here' autocomplete='off' required/> </label> <input type='submit' value='Find' /></form></p>" \



api.add_resource(StudentList, '/api/students', methods=['GET','POST'])
api.add_resource(Student, '/api/students/<int:student_id>', methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)  # setting debug=True will auto-reload the server when a file is changed




