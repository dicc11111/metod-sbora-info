import requests
import json
import vk


token = '69ca25aede71f2e4a3da7f4075feb127bfc1dd33587db46ede9dd65ea574d0995f094153fda7942360d00'
# Авторизуемся с помощью токена
session = vk.Session(access_token=token)
api = vk.API(session)
f = api.friends.get(user_id=30449019, v=5.131)
print(f)