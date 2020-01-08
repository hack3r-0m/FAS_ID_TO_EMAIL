from fedora.client.fas2 import AccountSystem
from fedora.client import AuthError

print("Login to your fedora account to use it as client")

USERNAME = input("ENTER YOUR FEDORA USERNAME :")
PASSWORD = input("ENTER YOUR FEDORA PASSWORD :")
FASCLIENT = AccountSystem(username=USERNAME, password=PASSWORD)

querry = input("ENTER USERNAME/FAS ID TO FIND EMAIL :")
ret_val = FASCLIENT.people_by_key(key='email', search=querry, fields=['id'])

print(ret_val.keys())
