# DOWNLOAD FLASK -- !!!ONLY DO THIS ONCE!!!
    # 1.) Open "Terminal"
    # 2.) Install flask module by typing "pip install flask"
    # 3.) If necessary for your machine or if prompted, download 
    #     the additional package by typing "pip install psycopg2-binary"

    # 4.) That's it, You're done!

# CREATE A NEW PYTHON FILE
    # 1.) Create a new python file using VSCode
    # 2.) Name the file -- "flask_tutorial.py"
            # 2.5.) You can name ^ this python file whatever you want .py, 
            # just remember that your command line inputs will be different!
            # Viewable down below \/


# IMPORT FLASK
from flask import Flask

# CREATE A NEW FLASK APP INSTANCE
app = Flask(__name__)

# CREATE OUR STARTING FLASK ROUTE using @app.route('/')
@app.route('/')

# CREATE A FUNCTION WITHIN THAT ROUTE BY PLACING IT UNDER THE ROUTE @app.route('')
def hello_world():
    return 'Hello World'

# HOW TO RUN OUR FLASK APP
    # 1.) Navigate to the directory that the app is in with the command line
    # 2.) Write "export FLASK_APP=flask_tutorial.py" in the command line
    # 3.) Write "set FLASK_APP=flask_tutorial.py" in the command line
    # 4.) Write "flask run" in the command line

# 🎉 Congratulations! You've successfully created your own locally-hosted website