import urllib.request
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'

origin=input("Enter Source:").replace(" ","+")
dest=input("Enter Destination:").replace(" ","+")

nav_request="origin={}&desitnation={}&key={}".format(origin, dest, api_key)
request = endpoint + nav_request

response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)
