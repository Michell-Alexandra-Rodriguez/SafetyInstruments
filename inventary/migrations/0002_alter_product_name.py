# Generated by Django 4.1 on 2022-09-07 02:15

from django.db import migrations, models
import generalvalidations.database_validations


class Migration(migrations.Migration):

    dependencies = [
        ('inventary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=70, unique=True, validators=[generalvalidations.database_validations.characters_size_should_be_grater_than_two]),
        ),
    ]
