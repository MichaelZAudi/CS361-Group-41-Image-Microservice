import requests

url_num = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/num'
url_event = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/event'
url_weighted = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/weighted'


def test_num(data):
    # send JSON data to server
    response = requests.post(url_num, json = data)

    in_data = response.json()

    if in_data.get('status') == 'success':
        print(f"Your random number is: {in_data.get('return_value')}")


def test_event(data):
    # send JSON data to server
    response = requests.post(url_event, json = data)

    in_data = response.json()

    if in_data.get('status') == 'success':
        print(f"Your random event is: {in_data.get('return_value')}")


def test_weighted(data):
    # send JSON data to server
    response = requests.post(url_weighted, json = data)

    in_data = response.json()

    if in_data.get('status') == 'success':
        print(f"Your weighted random event is: {in_data.get('return_value')}")


start, end = 1, 15
events = ['event_1', 'event_2', 'event_3', 'event_4']
weights = [20, 70, 5, 5]


print("Random int:")
test_num({'type': 'int', 'start': start, 'end': end})
print("Random float")
test_num({'type': 'float', 'start': start, 'end': end})
print("Random event:")
test_event({'events': events})
print("Weighted random event:")
test_weighted({'events': events, 'weights': weights})