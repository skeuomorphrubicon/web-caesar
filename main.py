from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action='/' method="POST">
        Rotate by:<input type="text" name="rot" value="0"><br>
        <br>
        <textarea name="text">{0}</textarea><br>
        <br>
        <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

@app.route("/", methods=['GET'])
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form.get("rot")
    text = request.form.get("text")
    text_str = str(text)
    rot_int = int(rot)
    encrypt_str = rotate_string(text_str, rot_int)
    return form.format(encrypt_str)


app.run()