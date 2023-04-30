import requests
import json

url = 'http://localhost:5000/add-transaction'
headers = {'Content-type': 'application/json'}

# Create the request body as a dictionary
data = {
    'productId': 1234,
    'parentId': 5678,
    'sender': '0x1234567890abcdef1234567890abcdef12345678',
    'receiver': '0xabcdef1234567890abcdef1234567890abcdef12'
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Send the POST request
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(response.json())
