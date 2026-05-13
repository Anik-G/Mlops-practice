from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course..."

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True)
    
    
###### log ########
# anik1@Anik_G MINGW64 /d/Dev/Mlops-practice/python/13-Flask/flask (main)
# $ python app.py
#  * Serving Flask app 'app'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 128-264-918
# 127.0.0.1 - - [13/May/2026 10:19:23] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [13/May/2026 10:19:23] "GET /favicon.ico HTTP/1.1" 404 -
# 127.0.0.1 - - [13/May/2026 10:19:36] "GET /index HTTP/1.1" 200 -
#  * Detected change in 'D:\\Dev\\Mlops-practice\\python\\13-Flask\\flask\\app.py', reloading
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 128-264-918
# 127.0.0.1 - - [13/May/2026 10:19:58] "GET / HTTP/1.1" 200 -