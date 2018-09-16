import urllib.request , json
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'
#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
#print(directions)
#keys of directions
dir_key=directions.keys()
#print(dir_key)
#Routes
routes=directions['routes']
#print(routes)
#Routes Keys
routes_key=routes[0].keys()
#print(routes_key)
#Leg or footway info
legs=routes[0]['legs']
#print(legs)
#print(len(legs))
#Total Distance Covered
dist=legs[0]['distance']['text']
print(dist)
