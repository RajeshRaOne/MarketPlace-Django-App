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
1. please use requirnment.txt file which are available in main folder for install dependencies 

```
pip install -r requirnements.txt
```

### Step 4: Apply Django Migrate command to create table in SQLite database  
1. go to project folder. mysite folder is project directory.


```
cd /mysite
python3 manage.py makemigrations
python3 manage.py migrate
```

  

### Step 6: Create Users and Friend list in SQLite database from json file date

1. This is manual process. you have to do this in manage.py shell. If db.sqlite3 file not present in  mysite folder. please follow setups to create users and friends list

```
python3 manage.py shell
```

### apply below python script in manage.py shell to migrate json file date to database 

Below python_migration script will migrate users.json in Friends List table and names.json in User table
 
```
data_migration_script.py
```

### 

Above python migration_script will create Users.username and password same as username which are available in names.json file.
It will create 100 users

```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey
```

2. To Create Admin username and password for accessing Django default admin page ( Optional )
Create this admin account after step: 1 migration completed.

```
python manage.py createsuperuser
```


### Step 7: Run Django Project using below command


```
python manage.py runserver
```

Open browser and access below URL

```
http://127.0.0.1:8000/login
```

### Step 8: You can use username for login. username and password both are same

```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey
```

### Step 8: We can add product in "Add items" menu .
you can login with different user account and add items

```
Example:
username: Krzysztof Gould
password: Krzysztof Gould

username: Kinga Ramsey
password: Kinga Ramsey
```
