<h1 align="center">🤖 Flask-RESTful template with SQLAlchemy 🤖</h1>
<div align="center">
  A simple default template for personal projects<br>
  <img src="https://user-images.githubusercontent.com/126655075/223354284-3a55f95b-cd0c-42ea-9ceb-3c1cb8c10129.png">
  <hr>
  
  ☑️ RestFUL • ☑️ SQLAlchemy • ☑️ Logging • ☑️ Docker • ☑️ CiCd
</div>

<br>

# ⭕ Installation & Requirements

## 🔹 Pre-Requirements
     - Tested with Python 3.10.7
     - Tested on Windows 10, 11 and Ubuntu 20.04
## 🔹 Installation
     - Clone the repository or use it as a template
     - Create repository secrets to login dockerhub (DOCKER_USERNAME, DOCKER_PASSWORD)
<br>

# ⭕ Usage And Settings/Options

## 🔹 .env
- Create your .env file in your container's folder
- The values below are given with representation purposes
### ◼️ DEBUG
```json
  "Debug=True"
  Or
  "Debug=False"
```
- With "True" value the app runs with the default runner in debug mode
- With "False" value given, the app uses waitress to run the app in production

### ◼️ HOST_PORT
```json
  "HOST_PORT": "5000"
```
- Specifies the port that the app will run on

### ◼️ HOST_ADDRESS
```json
  "HOST_ADDRESS": "0.0.0.0"
```
- Specifies the host address that the app will run on

### ◼️ DATABASE_URL
```json
  "DATABASE_URL": "mysql://root:root@flask-rest-temp_db:3306/flask-rest-temp"
```
- Specifies the database url that the app will connect to (mysql, postgresql, sqlite, etc.)

<br>

## 🔹 Usage
- Edit the docker-compose.yml file
  - Img name, You can also add your db- pma- etc. here
 
- Run the docker-compose.yml file
  - It will pull the image from dockerhub
  - After pulling, it starts the app and you can access it at host_address:host_port

<br><hr>

### ⭕ This template created for personal projects, but feel free to use and ask me if you have any question  ⭕
