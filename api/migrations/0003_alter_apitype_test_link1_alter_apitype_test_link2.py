# Generated by Django 4.0.4 on 2022-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_apitype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apitype',
            name='test_link1',
            field=models.URLField(help_text='Link to test the API', max_length=250, verbose_name='API Link 1'),
        ),
        migrations.AlterField(
            model_name='apitype',
            name='test_link2',
            field=models.URLField(help_text='Link to test the API', max_length=250, verbose_name='API Link 2'),
        ),
    ]
