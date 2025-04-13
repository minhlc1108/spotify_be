# Spotify Clone Backend

## Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/minhlc1108/spotify_be.git
cd spotify-be
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
```bash
psql -U postgres
CREATE DATABASE spotify_clone;
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

