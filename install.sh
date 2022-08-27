cd Online_Food_Ordering_System
clear
echo "Castle Food Orderring"
pip install -r requirements.txt
sudo pip install -r requirements.txt
echo "The superuser is Walter"
python manage.py migrate
python manage.py runserver