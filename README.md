# Marketplace App installation setup
### Step 1: Install Python 3
 
```
https://www.python.org/downloads/
```

### Step 2: Intall Virtual Environment and Activate 

```
pip install --user virtualenv
python3 -m venv env

mac/linux 
source env/bin/activate

windows
.\env\Scripts\activate
```
 

### Step 3: Install dependencies Module
1. please use requirnment.txt file to install dependencies 

```
pip install -r requirements.txt
```

### Step 4: Run Django Project using below command

```
python manage.py runserver
```

Open browser and access below URL

```
http://127.0.0.1:8000/login
```

### Step 5: You can use names.json users for login. username and password both are same.
You can use all users in users.json for login

```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey

username: Tyson Tomlinson
password: Tyson Tomlinson

Default Django Admin login
username: admin
password: admin
```

### Notes: New products can add by clicking "Add items" menu .
you can login with different user account and add items

```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey

username: Tyson Tomlinson
password: Tyson Tomlinson
```

### Notes: Product can be update or delete only by who added respective product
you can login with different user account and add items.


```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey

username: Tyson Tomlinson
password: Tyson Tomlinson
```

You can create and run docker image using below commands 

```
docker build --tag marketplace-mvp-app .
docker run --publish 8000:8000 marketplace-mvp-app
```

Open browser and access below URL

```
http://127.0.0.1:8000/login
```