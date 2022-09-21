# Business to Customer
# Transact between an M-Pesa short code to a phone number registered on M-Pesa
import credentials
import json
import requests
import mpesa_express



def submission(url, json_body):
    access_token = mpesa_express.generate_access_token()
    headers = {"Authorization": "Bearer %s" % access_token}
    if(access_token != '' or access_token != False):
        response = requests.post(url, json=json_body, headers=headers)
        return response
    else:
        print("Invalid access token")


def b2c_request(amount = 10, msisdn = 254726486929, remarks = 'payemployees'):

    data = {

        'InitiatorName' : credentials.b2c_initiator,
        'SecurityCredential' : 'SECURITY_CREDENTIAL',
        'CommandID' : 'SalaryPayment',
        'Amount' : amount,
        'PartyA' : credentials.bs_shortcode,
        'PartyB' : msisdn,
        'Remarks' : remarks, # mandatory
        'QueueTimeOutURL' : 'https://example.com/callback1',
        'ResultURL' : 'https://example.com/callback2',
        'Occasion' : '', # optional
    }    

    url = 'https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest';
    response = submission(url, data)
    return response

b2c_request()