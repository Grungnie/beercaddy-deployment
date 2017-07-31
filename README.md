# beercaddy-deployment

```
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

# Beer Caddy Redeployment
```
sudo service nginx stop
control c
git pull
gunicorn main:app -b 127.0.0.1:8080
sudo service nginx start
```