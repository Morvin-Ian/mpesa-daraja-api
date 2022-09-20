# Customer to Business
# Register validation and confirmation URLs on M-Pesa
import requests
import mpesa_express

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
    response = requests.post(url, json=data, headers=headers)
    return response.text

register_url()