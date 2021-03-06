# Generated by Django 3.0.3 on 2020-02-24 18:32

from django.db import migrations
from app0.models import RandomModel0, RandomModel1


def forwards(apps, schema_editor):
    RandomModel0.objects.get_or_create(int_field=123, float_field=789.23, char_field='asdfqwer')
    RandomModel0.objects.get_or_create(int_field=324, float_field=12.23, char_field='asdfzcv')
    RandomModel0.objects.get_or_create(int_field=12, float_field=334.23, char_field='zxcvasdf')
    RandomModel0.objects.get_or_create(int_field=12, float_field=884.0, char_field='poiu;lkj')
    RandomModel0.objects.get_or_create(int_field=99, float_field=2342.2, char_field='ertydfh')
    RandomModel0.objects.get_or_create(int_field=2234, float_field=234.23, char_field='09871234')
    last_model, _ = RandomModel0.objects.get_or_create(int_field=111, float_field=234.23, char_field='oiuykjh')
    RandomModel1.objects.get_or_create(char_field='asdfzxcv', fk_field=last_model)
    RandomModel1.objects.get_or_create(char_field='asdfv', fk_field=last_model)
    RandomModel1.objects.get_or_create(char_field=';lkjue', fk_field=last_model)
    RandomModel1.objects.get_or_create(char_field='asdfzhhhhww')
    RandomModel1.objects.get_or_create(char_field='000333asdfzam')


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
