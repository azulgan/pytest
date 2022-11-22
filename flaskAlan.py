from flask import Flask
from phue import Bridge

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><h1><a href='/api/gnagna'>gnagna</a></h1>"

@app.route("/api/gnagna")
def gnagna():
	return "<html></html>"

@app.route("/api/onoff")
def onoff():
    import requests
    r = requests.get('http://192.168.0.120/cm?cmnd=POWER+TOGGLE')
    return "done" #+(r.status_code)

@app.route("/api/lights/random")
def randomLight():
	import random
	b = Bridge()
	lights = b.get_light_objects()
	for light in lights:
		b.set_light(light)
		light.brightness = 254

