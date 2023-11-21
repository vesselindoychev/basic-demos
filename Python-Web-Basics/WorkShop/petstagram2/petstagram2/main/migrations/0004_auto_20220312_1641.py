# Generated by Django 3.2.12 on 2022-03-12 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20220312_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user', 'name')},
        ),
        migrations.RemoveField(
            model_name='pet',
            name='user_profile',
        ),
    ]
