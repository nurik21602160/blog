# Generated by Django 2.2.10 on 2020-04-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200412_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('П', 'Полик'), ('АШ', 'АвтоШторы'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
