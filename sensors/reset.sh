username="admin"
password="12345"
email="admin@example.com"

cd /opt/tutorial/ngrok-sensors/sensors

rm -rf db.sqlite3
rm -rf sensors/migrations

python3 manage.py makemigrations
python3 manage.py makemigrations sensors
python3 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${username}', '${email}', '${password}')" | python3 manage.py shell

#python3 manage.py loaddata fixtures/data.json
