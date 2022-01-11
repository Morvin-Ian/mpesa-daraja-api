from datetime import datetime
import base64

import credentials

import requests
from requests.auth import HTTPBasicAuth

def format_time():
    unformated_datetime=datetime.now()
    formated_datetime = unformated_datetime.strftime("%Y%m%d%H%M%S") #Formats the datetime i a format the safaricom expects
    return formated_datetime

def decode_password():
    pass_to_be_encoded = credentials.bs_shortcode + credentials.lnm_passkey + format_time() # The password exected is a combination of shortcode, the passkey, and the formated time
    #Encoding the password
    pass_encoded = base64.b64encode(pass_to_be_encoded.encode()) 
    #Decoding the password
    pass_decoded = pass_encoded.decode('utf_8') 
    return pass_decoded
 
def generate_access_token():
    response = requests.request("GET", credentials.acess_token_url, auth=HTTPBasicAuth(credentials.consumer_key,credentials.consumer_secrete))    
    res_json = response.json()
    #Filtering out the expiry date that is returned together with the access token as a response 
    filtered_access_token = res_json['access_token'] 
    return filtered_access_token
    
def mpesa():
    access_token = generate_access_token()
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {"Authorization": "Bearer %s" %access_token }


    request = {    
        "BusinessShortCode":credentials.bs_shortcode,    
        "Password":decode_password(),    
        "Timestamp":format_time(),    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":"1",    
        "PartyA":"2547xxxxxxx",    
        "PartyB":credentials.bs_shortcode,    
        "PhoneNumber":"2547xxxxxxxx",    
        "CallBackURL":"https://essaybees.com/home",    
        "AccountReference":"Morvin",    
        "TransactionDesc":"Pay library penalties"
    }

    response = requests.post(api_url, json=request, headers=headers) #The response can either be a succesful transaction or a failed transaction 
    print(response.text) #Check the reponse in your teminal

mpesa()
