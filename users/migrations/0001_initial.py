
import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(default='+996', max_length=14)),
                ('age', models.PositiveIntegerField(default=18, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(99)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('telegram', models.CharField(blank=True, max_length=100)),
                ('favorite_genre', models.CharField(max_length=100)),
                ('level', models.CharField(default='junior', max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
