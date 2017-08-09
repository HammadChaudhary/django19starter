mkdir trydjango19
cd trydjango19/
conda install -c anaconda virtualenv
virtualenv .
source bin/activate
pip freeze
pip install django==1.9
pip uninstall django
django-admin.py startproject trydjango19
cd trydjango19/
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp posts
#create model
python manage.py migrate
#no migrates to apply
python manage.py makemigrations
python manage.py migrate
python manage.py shell
