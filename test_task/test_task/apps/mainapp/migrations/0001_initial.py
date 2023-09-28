from django.db import migrations
from django.contrib.auth.models import User


import os
from dotenv import load_dotenv

def create_superuser(apps, schema_editor):

    load_dotenv()

    DJANGO_ADMIN_USERNAME = os.environ.get('DJANGO_ADMIN_USERNAME')
    DJANGO_ADMIN_PASSWORD = os.environ.get('DJANGO_ADMIN_PASSWORD')
    DJANGO_ADMIN_EMAIL = os.environ.get('DJANGO_ADMIN_EMAIL')

    User.objects.create_superuser(
        username=DJANGO_ADMIN_USERNAME,
        password=DJANGO_ADMIN_PASSWORD,
        email=DJANGO_ADMIN_EMAIL
    )

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spend', '0001_initial'), ('revenue', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]