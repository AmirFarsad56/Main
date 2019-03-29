# Generated by Django 2.1.4 on 2019-03-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190323_1707'),
        ('commonuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('picture', models.ImageField(default='commonuser/default/coverpicture/default_profile_pic.jpg', upload_to='commonuser/coverpicture')),
            ],
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='CommonUser',
        ),
    ]
