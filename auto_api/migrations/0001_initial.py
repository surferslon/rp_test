# Generated by Django 3.0.3 on 2020-02-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('int_field', models.IntegerField(blank=True, default=0, null=True)),
                ('float_field', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]
