# Email-Authentication

This webpage has been built in Django (Python).
It is an email authenticator i.e. it sends a one-time link to user's email for verification. Thereafter, it redirects the user to a login-logout dashboard. It also has the facility to view all users created till now.  


 ## Steps to Reproduce
* Start off by forking this repository and cloning it to get your local copy. Make sure you run this in git bash.

  ```bash
  $ git clone https://github.com/sagar-wal/Email-Authentication.git
  ```
* If you prefer a virtual-environment (venv) you should have pip and venv installed.

  ```bash
  $ sudo apt install python3-pip python3-dev
  $ sudo apt-get install python3-venv
  ```
 
* Navigate to the cloned repository directory and initiate a python 3 environment.
  
  ```bash
  $ python3 -m venv env 
  ```
* Activate your virtual environment.
  
  ```bash
  $ source env/bin/activate
  ```
  After successful activation, the code within parentheses will appear before the prompt in the bash similar to this:
  ```bash
  (env) <directory>$ 
  ``` 
  You can watch this video on how to install venv : <a href="https://www.youtube.com/watch?v=mqlCk_WCK2E">https://www.youtube.com/watch?v=mqlCk_WCK2E</a>
  
* Now install all requisites given in requirements.txt .

  ```bash
  $ cd Email-Authentication
  $ pip install -r requirements.txt
  ```

  Here is what your Pipfile will appear when you're ready to go ( you can view it by running $ pip freeze ).
  Please note there may be less packages in your list when you run $ pip freeze. The main required packages have been marked bold in the list. 

**Django==3.0**<br>
**python-dotenv==0.10.3**<br>
**six==1.13.0**<br>
asgiref==3.2.3<br>
certifi==2019.11.28<br>
chardet==3.0.4<br>
docopt==0.6.2<br>
gunicorn==20.0.4<br>
idna==2.8<br>
pipreqs==0.4.10<br>
pkg-resources==0.0.0<br>
psycopg2==2.8.4<br>
pytz==2019.3<br>
requests==2.22.0<br>
sqlparse==0.3.0<br>
urllib3==1.25.7<br>
whitenoise==4.1.2<br>
yarg==0.1.9

  Once the requirements are met, do the following :
  
 * Initialise the database
   
   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```
 * Create a file to store environment variables 
 
   ```bash
   $ touch .env 
   ```
 * Make sure to create one .gitignore file and add '.env' to it if you later plan to push this repository to the origin remote.
 
   ```bash
   $ echo .env >> .gitignore
   ```
   **Now come the most important steps**
   
 * Generate a secret key for the project
   
   Secret Key can be generated from <a href="https://miniwebtool.com/django-secret-key-generator/">here.</a>
   
   Generate the key and copy it to clipboard.
   
 * Add the secret key to the .env file

   ```bash
   $ echo 'SECRET_KEY="thesecretkeycopiedtoclipboard"' >> .env 
   ```
 * You now need to add your email address and password from which the confirmation email will be sent. Please be careful with this step as this is the most important step. Make sure correct email-address and password is given. 
 
   ```bash
   $ echo 'EMAIL_HOST_USER="youremailaddress"' >> .env
   $ echo 'EMAIL_HOST_PASSWORD="yourpassword"' >> .env
   ```
 
 * All set ! Now run the server and get started !
   
* Run the following command in your terminal.

  ```bash
  $ python manage.py runserver
  ```
  
* Navigate to http://localhost:8000 in any web browser to see it in action.Have fun!
