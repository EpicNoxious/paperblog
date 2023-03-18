echo "BUILD START"
python3.9 -m pip install -r requirements.txt


echo "MAKE MIGRATIONS"
python3.9 manage.py makemigrations blogs
python3.9 manage.py migrate blogs

echo "COLLECT STATIC"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
