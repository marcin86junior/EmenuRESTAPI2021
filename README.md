EmenuRESTAPI 
===========

![alt text](https://github.com/marcin86junior/EmenuRESTAPI/blob/main/readme.PNG?raw=true)

Wymagania:

	Python 3.8.x
	Django 3.0.7

Instalacja:

	utwórz nowy katalog "PythonRestEmenu" i wejdz do niego
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	wyłacz w urls.py (w myproject\myproject):      #path('', include('eMenu.urls')),
	cd myproject\
	python manage.py migrate
	python manage.py createsuperuser
	włacz w urls.py (w myproject\myproject):      path('', include('eMenu.urls')),
	python  manage.py loaddata eMenu\fixtures\data.json --app eMenu
	python manage.py runserver 

Testowanie:

	python manage.py test emnenu
	coverage run --source='.' manage.py test eMenu
	coverage raport -m

Wymagane poprawki:

	->dodać raportowanie / Celery+Redis (Heroku)
	->PostgreSQL (sprawdzić czy działa)
	->Docker (sprawdzić)
