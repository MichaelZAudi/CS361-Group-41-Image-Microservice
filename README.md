# CS361-Group-41-Randomizer-Microservice
# URLs:
* Random Number: https://cs361-group-41-randomizer-microservice.onrender.com/rand/num
* Random Event: https://cs361-group-41-randomizer-microservice.onrender.com/rand/event
* Weighted Random Event: https://cs361-group-41-randomizer-microservice.onrender.com/rand/weighted

## Requesting data:
* Main program sends a HTTP POST request to the url of the public server (hosted via Render) corresponding to the type of randomized result that they want. The request and all relevant information to it is stored in a JSON object, which is sent during the request.

* Required data: 
    * Random Number: 'type': 'int' || 'float', 'start': int, 'end': int >= 'start'
    * Random Event: 'events': {1+ event array}
    * Weighted Random Event: 'events': {1+ event array}, 'weights': {int array of weights equal in length to 'events' list}

* Example call in Python (Random Number):
```
import requests 

# Select url of desired randomization
url_server = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/num'

# Package data of request
request_data = {'type': 'int', 'start': 0, 'end': 12}

# Send request and save response
response = requests.post(url_server, json = request_data)

    *** continued below ***
 ```

## Receiving data:
* The microservice returns a JSON object containing the status of the request and the result of the request as a return_value.
* Example call in Python (Random Number):

```
    *** continued from above ***
    
# Parse data into a dictionary
incoming_data = response.json()

# Random number is the value of 'return_value' key 
if incoming_data.get('status') == 'success':
    print(f"Random Number: {incoming_data.get('return_value')}")
```

## UML sequence diagram:
![UML Diagram Randomization Microservice](Randomizer_UML.png)
