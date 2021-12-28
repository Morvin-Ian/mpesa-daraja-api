# Mpesa-Daraja-Api
Integrating the Daraja-Api with Python language.

## Credentials.py file
This file contains the consumer key and the consumer secrete key that is provided by Safaricom for test purposes.
https://developer.safaricom.co.ke/

## mpesa.py file
The main file that contains various functions with different tasks
according to the Daraja api requirements.

### format_time()
The datetime module in python returns a date in %Y-%m-%d %H%M%S format.
However the Daraja Api Docs dictates the timestamp format be in %Y%m%d%H%M%S format.
The function converts the current time according to the Api requirements.

### decode_password()
It utilizes the base64 import that that encodes and decodes the password.
The password is the combination of a business shortcode, the passkey, and the formated time (Daraja Api Docs).

### generate_access_token()
This function authenticates the request mate through the customer key and the customer secrete through HTTPBasicAuth.
The GET request made to the safaricom through the access_token url, gives a response that has the access token and the expiry time.
The access token is then filtered out.

### mpesa()
This function makes a GET request through the api_url and in relation to our request body, a response is provided by safaricom.
Below is a response to a successfull request.

![Screenshot at 2021-10-25 21-26-04](https://user-images.githubusercontent.com/78966128/138972862-2ac78448-de8c-463a-86b8-de4c321feece.png)

## Requirements
1. requests module  
2. datetime module  
3. base64 module  

This Api has been applied in this [library website](https://rulibrary.herokuapp.com)
