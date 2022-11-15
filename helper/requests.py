
import threading , requests
from django.core.mail import send_mail

class HandleThreads(threading.Thread):
    def __init__(self , message , subject , recipientList):
        self.message = message
        self.subject = subject
        self.recipientList = recipientList
        threading.Thread.__init__(self)
    
    def run(self):
        from_email = 'ayaelkilany735@gmail.com'
        send_mail(self.message, self.subject, from_email ,self.recipientList , fail_silently=False)
        

def AuthenticationToken():
    payload = {
    "api_key" : "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnVZVzFsSWpvaU1UVTFNelU0T0RVMU5pNHdNemcxTmpJaUxDSndjbTltYVd4bFgzQnJJam96TURZeExDSmpiR0Z6Y3lJNklrMWxjbU5vWVc1MEluMC5hQUVSSVVjdVZlVl9kb3ZnZ3FfZFB4T3JSUm80UjJLdUNlRlNiMDMzMzd3WDg1WnBJb3VxMS11TXV4UjJVVngxWldYQlQ1cnhoZ1IxTVlLNW9QNHJrdw=="
    }
    response = requests.post("https://accept.paymob.com/api/auth/tokens" , json=payload)
    response_json = response.json()
    token = response_json['token']
    return token

def OrderRegistration(token , amount_cents , items ,delivery_needed=False ):
    payload = {
        'auth_token' : token,
        'delivery_needed' : delivery_needed,
        'amount_cents' : amount_cents,
        'items' : items,
    }
    response = requests.post("https://accept.paymob.com/api/ecommerce/orders" , json=payload)
    response_json = response.json()
    order_reg_id = response_json['id']
    return order_reg_id


def GetPaymentKey(order_reg_id , token , amount_cents , currency , client_name):
    payload = {
        'auth_token' : token,
        'amount_cents' : amount_cents,
        'expiration' : 3600,
        'order_id' : order_reg_id,
        'billing_data' : {
            'first_name' : client_name,
            "apartment": "803", 
            "email": "claudette09@exa.com", 
            "floor": "42",
            "street": "Ethan Land", 
            "building": "8028", 
            "phone_number": "+86(8)9135210487", 
            "shipping_method": "PKG", 
            "postal_code": "01898", 
            "city": "Jaskolskiburgh", 
            "country": "CR", 
            "last_name": "Nicolas", 
            "state": "Utah"
        },
        'currency' : currency,
        'integration_id' : '4658'
    }
    
    response = requests.post("https://accept.paymob.com/api/acceptance/payment_keys" , json=payload)
    response_json = response.json()
    payment_token = response_json['token']
    
    return payment_token


def CreateIFrame(payment_token):
    payload = {
        "payment_token" : payment_token
    }
    response = requests.post("https://accept.paymob.com/api/acceptance/iframes/29754?" , params=payload)
    return response.url