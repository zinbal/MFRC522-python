import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
from datetime import datetime
from flask import redirect
from flask import Flask

now = datetime.now()
app = Flask(__name__)

#str k=" "
def read():
    CardReader = SimpleMFRC522()
    print ('Scanning for a  card..')
    print ('to cancel press ctrl+c')
    try:
            id, text = CardReader.read()
            #print(text)
    finally:
            gpio.cleanup()
    return str(id)
    
    
@app.route("/")
def index():

    ptr = "<!DOCTYPE html> <html>\n";
    ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
    ptr +="<title>Automation Setup</title>\n";
    ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
    ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
    ptr +=".button {display: block;width: 80px;background-color: #1abc9c;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
    ptr +=".button-on {background-color: #1abc9c;}\n";
    ptr +=".button-on:active {background-color: #16a085;}\n";
    ptr +=".button-off {background-color: #34495e;}\n";
    ptr +=".button-off:active {background-color: #2c3e50;}\n";
    ptr +="p {font-size: 14px;color: #888;margin-bottom: 5px;}\n";
    ptr +="</style>\n";
    ptr +="</head>\n";ptr +="<body>\n";
    ptr +="<h1>RASPBERRY flask Web Server</h1>\n";
    ptr +="<h3>FETCH DATA</h3>\n";
    
    ptr +="<p>CLICK TO GET INPUT</p><a class=\"button button-off\" href=\"fetch\">Read</a>\t\n";
    ptr +="<p>CLICK TO GET DATA</p><a class=\"button button-off\" href=\"data\">Fetch</a>\t\n";
    ptr +="</body>\n";
    ptr +="</html>\n";
    return ptr

@app.route("/data")

def data():
    file = open("soup.txt", "r")
    ptr=" "
    k=file.read()
    for line in k.splitlines():
        ptr+="<p>"+str(line)+"</p>";
    return ptr

@app.route("/fetch")

def fetch():
    ptr = "<!DOCTYPE html> <html>\n";
    a=read()
    if a=="523992995976":
        a="Harsh"
    elif a=="236952773122":
        a="Varnit"
    current_time = now.strftime("%H:%M:%S")
    k=a+"\t"+current_time+"\n"
    file = open('soup.txt','a')
    file.write(k)
    file.close()
    return redirect("/")
app.run(port=8000)
