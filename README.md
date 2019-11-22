# Airbnb Clone
```
Cloning Airbnb with Python, Django, Tailwind and more...
Last README update 19.11.22
```

# Installation

### pipenv
```bash
pipenv --three                  // python version 3
pipenv install django==2.2.6    // django version
pipenv shell                    // Enter a bubble
```

### Third Party App
```bash
pip install django-seed
pip install django-countries
pip install Pillow
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
python manage.py seed_list --number 50
python manage.py seed_reservations --number 50
```
