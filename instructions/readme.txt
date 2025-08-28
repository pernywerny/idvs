core dependencies
Python packages
	Django
	Django rest framework
	mysqlclient
	pytz




Running the application

1. Install python and add it to path
2. install dependencies packages
3. The api and portal are separate applications but both needs to be run simultaneously
4. Open shell/cmd in the api's root directory and type "py manage.py runserver 127.0.0.1:8000"
5. Open shell/cmd in the portal's root directory and type "py manage.py runserver 127.0.0.1:8080"
6. Launch your browser application and go to "http://127.0.0.1:8080/user-manager/auth/public/login"




Database
The application uses MariaDB so it serves the database from port 3306, serving your database from any other port will cause the application to fail.

You can update the database settings if you wish in the setting.py files that can be found in "IDVS/IDVS" and "portal/portal"

Avoid changing any other settings as this may break the app


to create the database from scratch: 
	1. create your database using the create db command
	2. open shell/cmd application and type "py manage.py migrate" 
	3. add data




Admin App
Both the portal and api have individual admin sites access them by going to "http://application_url:<port>/admin"

create an admin user by running "py manage.py createsuperuser --u <your_username>
