# Spotify Clone Backend

## Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/minhlc1108/spotify_be.git
cd spotify_be
```
### 2. Create and Activate Virtual Environment
```bash
python3.12 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup Database
Login to PostgreSQL
```bash
sudo -i -u postgres
```
Create a new user
```bash
CREATE USER myuser WITH PASSWORD 'mypassword';
```
Create a new database
```bash
CREATE DATABASE mydatabase;
```
Grant privileges to the user
```bash
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```
Exit psql
```bash
\q
```
### 5. Configure environment variables
Create a `.env` file in the root directory based on the `.env.example` file provided.
```bash
cp .env.example .env
```
Then, open the .env file and update the values as needed. 
### 5. Apply database migrations
```bash
python manage.py migrate
```
### 6. Create a superuser
```bash
python manage.py createsuperuser
```
### 7. Run the server
```bash
python manage.py runserver
```
Access the Admin Interface: Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

