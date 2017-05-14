See result in kypoheko.pythonanywhere.com

git clone https://github.com/KypoHeko/hive-repo.git

--//--//--

(optional)
```
pip install virtualenv
python -m venv myvenv
cd myvenv/activate
cd ..
cd ..
```

--//--//--

pip install -r requirements.txt

python manage.py migrate

python manage.py shell

from honey.models import Persona

Persona()._bootstrap(count=250, gender='female')

quit()

python manage.py runserver
