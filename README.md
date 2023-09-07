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
make tests
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


## Testing:

Para ejecutar los test unitarios de todo el proyecto:

```
make tests
```

Si queremos ejecutar con nivel de detalle los test de una app en particular:

```
python manage.py test products.tests.test_views --settings=settings.local -v  2
```
usando make

```
make test-one TEST_NAME=products.tests.test_views
```
