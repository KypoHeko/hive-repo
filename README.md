# Hive - Experimental social network

See result in kypoheko.pythonanywhere.com

## Running the Project Locally
Clone the repository:
```
git clone https://github.com/KypoHeko/hive-repo.git
```

Create virtual environment:
```
pip install virtualenv
python -m venv myvenv
source myvenv/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Create the database:
```
python manage.py migrate
```

Create dummy data:
```
python manage.py shell
from honey.models import Persona
Persona()._bootstrap(count=250, gender='female')
quit()
```

Run server:
```
python manage.py runserver
```
