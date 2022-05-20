from configurations import values


class DataBaseSettings:
    POSTGRES_DB = values.Value(environ_prefix='')
    POSTGRES_USER = values.Value(environ_prefix='')
    POSTGRES_PASSWORD = values.Value(environ_prefix='')
    DATABASE_HOST = values.Value()
    DATABASE_PORT = values.PositiveIntegerValue()
    CONN_MAX_AGE = values.PositiveIntegerValue()

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': self.POSTGRES_DB,
                'USER': self.POSTGRES_USER,
                'PASSWORD': self.POSTGRES_PASSWORD,
                'HOST': self.DATABASE_HOST,
                'PORT': self.DATABASE_PORT,
                'CONN_MAX_AGE': self.CONN_MAX_AGE,
                'OPTIONS': {
                    'connect_timeout': 10,
                    'options': '-c statement_timeout=15000ms',
                },
            }
        }
