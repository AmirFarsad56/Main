# Generated by Django 2.1.4 on 2019-03-23 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20190323_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('picture', models.ImageField(default='commonuser/default/coverpicture', upload_to='commonuser/coverpicture')),
            ],
        ),
    ]
