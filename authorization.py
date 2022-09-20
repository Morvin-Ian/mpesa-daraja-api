import requests
import credentials
import base64


url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
querystring = {"grant_type":"client_credentials"}
payload = ""

auth = f"{credentials.consumer_key}:{credentials.consumer_secrete}"
encoded_auth = base64.b64encode(auth.encode())
decoded_auth = encoded_auth.decode()
headers = {"Authorization": f"Basic {decoded_auth}"}


response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text)