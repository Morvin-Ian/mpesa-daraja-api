# Customer to Business
# Register validation and confirmation URLs on M-Pesa

import requests
import mpesa_express
import credentials
import json


def register_url():
    access_token = mpesa_express.generate_access_token()
    data = {
        
        'ShortCode' : 'LNM_SHORTCODE',
        'ResponseType' : 'Completed',
        'ConfirmationURL' : 'https://example.com/callback-c2b',
        'ValidationURL' : 'https://example.com/callback-c2b',
    }

    url = 'https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    headers = {"Authorization": "Bearer %s" % access_token}
    response = submission(url, data)
    return response

def submission(url, json_body):
    access_token = mpesa_express.generate_access_token()
    headers = {"Authorization": "Bearer %s" % access_token}
    if(access_token != '' or access_token != False):
        response = requests.post(url, json=json_body, headers=headers)
        return response
    else:
        print("Invalid access token")


def simulate_c2b(amount = 10, msisdn = 254726486929, ref = 'Testing'):

    data = {
        'ShortCode' : credentials.bs_shortcode,
        'CommandID' : 'CustomerPayBillOnline',
        'Amount' : amount,
        'Msisdn' : msisdn,
        'BillRefNumber' : ref, # account number
    }
    data = json.loads(data)
    url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
    response = submission(url, data)
    return response


def initiate_stk(amount = 10, msisdn = 254726486929, ref = 'account'):
 
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    request = {    
        "BusinessShortCode":credentials.bs_shortcode,    
        "Password": mpesa_express.decode_password(),    
        "Timestamp":mpesa_express.format_time(),    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":amount,    
        "PartyA":msisdn,    
        "PartyB":credentials.bs_shortcode,    
        "PhoneNumber":msisdn,    
        "CallBackURL":"https://essaybees.com/home",    
        "AccountReference":ref,    
        "TransactionDesc":"Pay library penalties"
    }

    response = submission(api_url,request) #The response can either be a succesful transaction or a failed transaction 
    return response

simulate_c2b()