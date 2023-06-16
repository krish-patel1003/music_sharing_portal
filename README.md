
# Music Sharing Portal



## Documentation
Link: https://documenter.getpostman.com/view/26223290/2s93shz9z8

The link has a "Run in Postman" button on top right, using which the APIs can be tested.
## Run Locally

Create virtual environment

```bash
  virtualenv venv
```

Activate virtual environment

```bash
  .\venv\Scripts\activate
```

Clone the project

```bash
  git clone https://github.com/krish-patel1003/music_sharing_portal.git
```

Go to the project directory

```bash
  cd music_sharing_portal
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
  python manage.py runserver
```


