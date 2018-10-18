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
        <form method="POST">Rotate by:<input type="text" name="rot" value="0"><br>
        <br>
        <textarea name="text">{0}</textarea><br>
        <br>
        <input type="submit" value="Submit">
        </form>
      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/", methods=['GET'])
def index():
    return form.format("")
index()

app.run()

@app.route("/", methods=['POST'])
def encrypt(x, y):
    text_str = str(y)
    rot_int = int(x)
    encrypt_str = "<h1>" + rotate_string(text_str, rot_int) + "</h1>"
    return form.format(encrypt_str)
encrypt(rot,text)