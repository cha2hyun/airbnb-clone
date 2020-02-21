# Airbnb Clone

```
LINK : http://airbnb-clone.sim3mek5vx.ap-northeast-2.elasticbeanstalk.com/
```

```
Cloning Airbnb with Python, Django, Tailwind and more...
```

# Installation

### first installation

```bash
MAC OS X
1. install iterm2
2. install oh my zsh
3. setting the shell
4. install brew
5. install pipenv
6. install java sdk
7. install git

```

### pipenv

```bash
brew install pipenv
pipenv --three                  // python version 3
pipenv install django==2.2.6    // django version
pipenv shell                    // Enter a bubble
```

### Third Party App

```bash
pip install django-seed
pip install django-countries
pip install Pillow
pip install django-dotenv
pip install requests
```

### Initialize

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8080
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

### EMAIL

```bash
mailgun.com
ID : cha2hyun.dev@gmail.com
```

### Todo later

```bash
verify_email.html 꾸미기
git login 수정하기
Edit-Profile Avatar 수정
Edit-Password 에서 Placeholder 적용해보기 - form 만들어야함
edit photo에서 사진 수정하기
edit room에서 delete room 만들어보기
delete시 정말 삭제하겠습니까 메세지창 띄워보기
enc-type 이 무엇인지 확인해보기
css grid 강의 보기
예약할때 자바스크립트 이용해서 하루 이상 가능하게 해보기, 체크인, 체크아웃 지정해서 range 설정
AWS 환경변수 이용해서 admin/ 주소 계속 랜덤으로 바꾸기
AWS 환경변수에 ID, KEY 업로드
큰 용량 업로드 되는걸 방지 django-imagemagick 사용, 포맷 바꾸기 django-imagemit
서치바 수정
```

### Tailwind CSS Installation

```bash
1. install node.js
2. sudo pip install npm
3. npm init (outside of pipenv)
4. npm install gulp gulp-postcss gulp-sass gulp-csso node-sass -D
5. npm install tailwindcss -D
6. sudo npm install -g npx
7. npx tailwind init
8. npm install autoprefixer -D
9. npm run css
```

### Locale

```
Install GNU gettext : brew install gettext
Create symlink : brew link gettext --force
django-admin makemessage --locale==ko,en,..등등
수정후 django-admin compilemessages
```

### AWS SERVER

```
pipenv install awsebcli --dev
eb init
eb create 이름
eb deploy
```

06_seed_facilities:
command: "django-admin seed_facilities"
07_seed_roomtypes:
command: "django-admin seed_roomtypes"
071_seed_amenities:
command: "django-admin seed_amenities"
08_seed_users:
command: "django-admin seed_users --number 150"
09_seed_rooms:
command: "django-admin seed_rooms --number 250"
10_seed_reviews:
command: "django-admin seed_reviews --number 250"
11_seed_lists:
command: "django-admin seed_lists"
12_seed_reservations:
command: "django-admin seed_reservations --number 250"
13_seed_avatar_delete:
command: "django-admin seed_avatars"

container_commands:
01_migrate:
command: "django-admin migrate"
leader_only: true
02_compilemessages:
command: "django-admin compilemessages"
