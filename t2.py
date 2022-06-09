import requests

def get_api_key(email: str, passwd: str):
   headers = {
       'email': email,
       'password': passwd,
   }
   res = requests.get('https://petfriends.skillfactory.ru//api/key', headers=headers)
   status = res.status_code
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   return status, result


print(get_api_key('oleg-g@yandex.ru','667667667'))

# (200, {'key': '391390ab6c8b36506c2baa9be5b9005961d0e97fd0b66a3f3ff66e38'})