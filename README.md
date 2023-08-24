# Ejercicio práctico de Django

## Instalación:

```
python -m venv env

# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate

pip install -r requirements.txt

make migrate
make run
```

Para crear un super usuario y acceder al admin:

```
make createsuperuser
```

## Base de datos:

Esto proyecto requiere que tenga instalado MySQL.
Actualice los datos de la base de datos que quiere utilizar en `settings/local.py`.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            "read_default_file": "path/to/my.cnf",
        }
    }
}
```

```
# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

docs: https://docs.djangoproject.com/en/4.2/ref/databases/#mysql-notes

## Diagrama de la base de datos:

![Diagrama base de datos](docs/db.png)
