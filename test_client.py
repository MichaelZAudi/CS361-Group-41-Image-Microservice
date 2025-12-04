import requests

url_prompt = 'https://cs361-group-41-image-microservice.onrender.com/image/prompt'


def test_event(data):
    # send JSON data to server
    response = requests.post(url_prompt, json = data)

    in_data = response.json()

    if in_data.get('status') == 'success':
        print(f"Your random event is: {in_data.get('return_value')}")


image = test_event({'prompt': "Generate a baseball card for a player named Josh on the Cats team."})
print(image)