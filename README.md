
git clone git@github.com:vccabral/django-unchained.git
vagrant up
vagrant ssh
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
