mkdir park
cd park
virtualenv ./flask/ -p python3
source flask/bin/activate
pip install flask
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
chmod a+x app.py
