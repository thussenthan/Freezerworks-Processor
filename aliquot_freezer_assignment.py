# %%
import base64
import csv
import requests

username = "demoUser"
password = "demoPassword"

# Bearer Token (JWT) Authentication
jwt_url = "https://localhost/api/v1/users/authenticate"
encodedUserPass = base64.b64encode(f'{username}:{password}'.encode())
headers = {``
  "Content-Type": "application/json",
  "Authorization": "Basic " + encodedUserPass.decode()
}
response = requests.request("GET", jwt_url, headers=headers)
jwt = response.json()['properties']['token']


def update_aliquot(aliquot_id, rack, box, position):
    url = f"https://UPDATE_UPDATE_UPDATE/api/v1/aliquots/{aliquot_id}" # UPDATE!!!

    payload = {
        "fwLocation": {
            "FK_FreezerSectID": 'Sholler Cryofreezer1',
            "position1": rack,
            "position2": box,
            "position3": position
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + jwt
    }

    response = requests.post(url, json=payload, headers=headers) # Might need to use requests.request("POST"...
    print(response.text)
    return response.text

# Read CSV and update aliquots
csv_file_path = 'Aliquot Freezer Assignment.csv'  # Replace with your CSV file path

with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        aliquot_id = row['Aliquot ID']
        rack = row['Rack']
        box = row['Box']
        position = row['Position']

        result = update_aliquot(aliquot_id, rack, box, position)
        print(f"Updated aliquot {aliquot_id}: {result}")





# %%

# importing the requests module because it is a little friendlier than the
# built-in http.client module
import base64
import requests

# hard code a few variables here for demo purposes:
username = "demoUser"
password = "demoPassword"


#######################################################################
################  Request 1: Authentication ###########################
#######################################################################
# First thing, request a JWT. We'll need that to make more requests.
# This is one of the few endpoints that requires us to send the username
# and password. Once we have the JWT we'll use that instead.
jwt_url = "https://localhost/api/v1/users/authenticate"

# Build the headers we'll send with our request. Here we need to let the API
# know we're sending JSON formatted data and provide the Authorization info.
# Base64 encode the username and password in this format: username:password
# Note that for this Python function it needs to be a bytes like object.
encodedUserPass = base64.b64encode(f'{username}:{password}'.encode())  # ZGVtb1VzZXI6ZGVtb1Bhc3N3b3Jk
headers = {
  "Content-Type": "application/json",
  "Authorization": "Basic " + encodedUserPass.decode()
}

# Make the request to the API
response = requests.request("GET", jwt_url, headers=headers)

# The response will be Siren formatted. See the Responses section for more.
# Convert the response from text to JSON (really a Python dict) and then pull out the token.
# Here, we are assuming success. In real code we'd need to check for errors.
jwt = response.json()['properties']['token']


#######################################################################
############  Request 2: Aliquots for a Sample  #######################
#######################################################################
# Now that we have our token, we can make requests to other endpoints using
# bearer token auth.

# Let's get all the aliquots that belong to a particular Sample with
# a Freezerworks ID of 100001.
sample_url = "https://localhost/api/v1/samples/100001"

# Note for this request we are using a different authorization header value.
# Also note that we haven't done anything with the JWT token. I don't need to
# read it or edit it, just send it back with the next request.
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + jwt
}

sample_detail_response = requests.request("GET", sample_url, headers=headers)

# We can do the same conversion of the response and then iterate over all the aliquots
# belonging to this sample to build a list of aliquot numbers.
aliquots_to_check = []
for aliquot in sample_detail_response.json()['properties']['aliquots']:
    aliquots_to_check.append(aliquot['PK_AliquotUID'])


#######################################################################
############   Request 3: Verify the Aliquots   #######################
#######################################################################
# Next we can take our list of aliquots and see if they are available to be requisitioned
# We don't need to make any update to our 'headers' this time, but we do need to build a
# body payload and make a POST request to send it in.
verify_url = "https://localhost/api/v1/aliquots/verifyAction"

payload = {
    "values": aliquots_to_check,
    "fieldName": "PK_AliquotUID",
    "action": "requisition"
}

verify_response = requests.request("POST", verify_url, json=payload, headers=headers)

# With our final response from the API, we can print the list of aliquots which
# can be requisitioned. In a real application we could then take those aliquots
# and make request for them in Freezerworks, or generate and print labels for
# them, or integrate with another system to notify them that these aliquots meet
# their requirements.
print(verify_response.json()['properties']['aliquots']['verified'])

