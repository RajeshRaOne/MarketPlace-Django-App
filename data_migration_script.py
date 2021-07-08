# use this script in python manage.py shell

from django.contrib.auth.models import User
import json
from marketplace.models import products,Friends
jsonDec = json.decoder.JSONDecoder()

#add names.json data path
name_file = open('./data/names.json')
name_data = json.load(name_file)

for i in name_data:
    user = User.objects.create_user(username=i['name'],password=i['name']) 
    user.save()

#view added user details
objects = User.objects.all()                                   
for i in objects:
    print(i.username)
    
#add users.json data path
user_file = open('./data/names.json')
user_data = json.load(user_file)
# print(type(user_data))
    
for i in user_data:
    friends = Friends(user_id=i['id'],friends_list=json.dumps(i['following']))
    friends.save()
    
friends_obj = Friends.objects.all()
for i in friends_obj:
    print((jsonDec.decode(i.friends_list))