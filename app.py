from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        student_id = request.form['student_id']
        course = request.form['course']
        department = request.form['department']
        qualification = request.form['qualification']
        marks = request.form['marks']

        return render_template_string("""
        <html>
        <head>
            <title>Registration Successful</title>
            <style>
                body {
                    font-family: Arial;
                    background: #e8f0fe;
                    text-align: center;
                    padding: 30px;
                }

                .box {
                    background: white;
                    padding: 30px;
                    max-width: 600px;
                    margin: auto;
                    border-radius: 12px;
                }

                h1 {
                    color: green;
                }

                p {
                    font-size: 17px;
                    text-align: left;
                }
            </style>
        </head>

        <body>
            <div class="box">
                <h1>Registration Successful!</h1>

                <h2>Student Details</h2>

                <h3>Personal Information</h3>

                <p>Full Name: {{ name }}</p>
                <p>Date of Birth: {{ dob }}</p>
                <p>Gender: {{ gender }}</p>
                <p>Email: {{ email }}</p>
                <p>Phone: {{ phone }}</p>
                <p>Address: {{ address }}</p>

                <h3>Academic Information</h3>

                <p>Student ID: {{ student_id }}</p>
                <p>Course: {{ course }}</p>
                <p>Department: {{ department }}</p>
                <p>Qualification: {{ qualification }}</p>
                <p>Marks: {{ marks }}</p>

                <h2>Thank you for registering!</h2>

                <a href="/">Register Another Student</a>
            </div>
        </body>
        </html>
        """,
        name=name,
        dob=dob,
        gender=gender,
        email=email,
        phone=phone,
        address=address,
        student_id=student_id,
        course=course,
        department=department,
        qualification=qualification,
        marks=marks
        )

    return render_template_string("""
    <html>
    <head>
        <title>Student Registration</title>

        <style>
            body {
                font-family: Arial;
                background: #e8f0fe;
                padding: 20px;
            }

            .container {
                background: white;
                max-width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
            }

            h1 {
                text-align: center;
                color: #1a237e;
            }

            h3 {
                color: #303f9f;
            }

            input, select, textarea {
                width: 100%;
                padding: 12px;
                margin: 8px 0 15px;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            button {
                background: #1a237e;
                color: white;
                padding: 14px;
                width: 100%;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background: #3949ab;
            }
        </style>
    </head>

    <body>

    <div class="container">

        <h1>Student Registration Form</h1>

        <form method="POST">

            <h3>Personal Details</h3>

            <label>Full Name</label>
            <input type="text" name="name" required>

            <label>Date of Birth</label>
            <input type="date" name="dob" required>

            <label>Gender</label>
            <select name="gender" required>
                <option value="">Select Gender</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
            </select>

            <label>Email Address</label>
            <input type="email" name="email" required>

            <label>Phone Number</label>
            <input type="tel" name="phone" required>

            <label>Address</label>
            <textarea name="address" required></textarea>

            <h3>Academic Details</h3>

            <label>Student ID</label>
            <input type="text" name="student_id" required>

            <label>Course</label>
            <select name="course" required>
                <option value="">Select Course</option>
                <option>B.Tech</option>
                <option>BCA</option>
                <option>MCA</option>
                <option>MBA</option>
                <option>BBA</option>
            </select>

            <label>Department</label>
            <input type="text" name="department" required>

            <label>Previous Qualification</label>
            <input type="text" name="qualification" required>

            <label>Percentage / Marks</label>
            <input type="number" name="marks"
                   min="0" max="100" step="0.01" required>

            <button type="submit">
                Submit Registration
            </button>

        </form>

    </div>

    </body>
    </html>
    """)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)