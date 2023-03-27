# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

import dj_database_url
from project.env import config

DATABASE_URL = config("DATABASE_URL", default=None)
if DATABASE_URL is not None:
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_health_checks=True,
            conn_max_age=600,
        )
    }


# {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": "neondb",
#             "USER": "hodaeyfha",
#             "PASSWORD": "YfASQ2Wjab0t",
#             "HOST": "ep-hidden-unit-978731.us-east-2.aws.neon.tech",
#             "PORT": "5432",
#         }
