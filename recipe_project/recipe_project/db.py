
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL={
    'default':{
        'client_encoding':'UTF8',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'recipe_test',
        'USER':'postgres',
        'PASSWORD':'postgres',
        'HOST':'localhost'
    }
}
