```sh
python3.12 -m venv .env
source .env/bin/activate
# https://www.toptal.com/developers/gitignore/
touch .gitignore && code .gitignore  

git init

git add .
git commit -m "git init, .gitignore generado con gitignore.io, .env creado"
```

```sh
python3.12 -m pip install --upgrade pip
pip install django
pip freeze > requirements.txt
```

```sh
django-admin startproject backend_adopta_un_junior
cd backend_adopta_un_junior    
```