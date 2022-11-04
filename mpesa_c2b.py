#Confirmation and validaion url must be registered first
import json
import requests
import credentials
from mpesa_express import generate_access_token



def register_url():
    access_token = generate_access_token()
    data = {
        
        'ShortCode' : credentials.registration_shortcode,
        'ResponseType' : 'Completed',
        'ConfirmationURL' : 'https://fullstackdjango.com/confirmation',
        'ValidationURL' : 'https://fullstackdjango.com/validation',
    }

    url = credentials.registration_url
    header = {"Authorization": "Bearer %s" %access_token, 'Content-Type': "application/json" }
    response = requests.post(url, json=data, headers=header)
    return response.text


def simulate_c2b():
    access_token = generate_access_token()
    data = {
        'ShortCode' : credentials.registration_shortcode,
        'CommandID' : 'CustomerPayBillOnline',
        'Amount' : "1",
        'Msisdn' : 254726486929,
        'BillRefNumber' : "ref", # account number
    }

    header = {"Authorization": "Bearer %s" %access_token, 'Content-Type': "application/json" }
    url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
    response = requests.post(url, json=data, headers=header)
    return response.text
