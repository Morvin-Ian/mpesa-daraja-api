# M-PESA EXPRESS
# This ApiInitiates online payment on behalf of a customer.
# The Daraja Api requires a formatted time, a paassword, and an access token

from datetime import datetime
import base64
import json
import pprint

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
    response = requests.get(credentials.acess_token_url, auth=HTTPBasicAuth(credentials.consumer_key,credentials.consumer_secrete))    
    res_json = response.json()
    #Filtering out the expiry date that is returned together with the access token as a response 
    filtered_access_token = res_json['access_token'] 
    return filtered_access_token
    
def initiate_stk():
    access_token = generate_access_token()
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {"Authorization": "Bearer %s" %access_token }


    request = {    
        "BusinessShortCode":credentials.bs_shortcode,    
        "Password":decode_password(),    
        "Timestamp":format_time(),    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":"1",    
        "PartyA":"254726486929",    
        "PartyB":credentials.bs_shortcode,    
        "PhoneNumber":"254726486929",    
        "CallBackURL":"https://essaybees.com/home",    
        "AccountReference":"Morvin",    
        "TransactionDesc":"Pay library penalties"
    }

    response = requests.post(api_url, json=request, headers=headers) #The response can either be a succesful transaction or a failed transaction 
    string_response = response.text
    data_object = json.loads(string_response)
     
    merchant_request_id = data_object["MerchantRequestID"]
    checkout_request_id = data_object["CheckoutRequestID"]
    response_code = data_object["ResponseCode"]
    response_description = data_object["ResponseDescription"]
    customer_message = data_object["CustomerMessage"]

    data = {
        "MerchantRequestID": merchant_request_id,
        "CheckoutRequestID": checkout_request_id,
        "ResponseCode": response_code,
        "ResponseDescription": response_description,
        "CustomerMessage": customer_message,
    } 

    pprint.pprint(data)

initiate_stk()
