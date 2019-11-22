# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more...

## Installation

### pipenv

```bash
$ sudo -H pip install pipenv
```

```bash
$ pipenv install --python $(which python3.7)
```

### Pillow Prerequisites

https://pillow.readthedocs.io/en/stable/installation.html

on Ubuntu 16.04 LTS

```bash
$ sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    libharfbuzz-dev libfribidi-dev
```

### Initialize

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Seeding items

```bash
python manage.py seed_amenities
python manage.py seed_facilities
python manage.py seed_roomtypes
```

```bash
python manage.py seed_users --number 50
python manage.py seed_rooms --number 150
```

```bash
python manage.py seed_reviews --number 50
python manage.py seed_lists --number 50
python manage.py seed_reservations --number 50
```
