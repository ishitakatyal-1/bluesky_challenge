# Generated by Django 3.2.5 on 2021-11-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissioncategories',
            name='category_alias',
            field=models.CharField(blank=True, help_text='Alias for category', max_length=10, null=True, verbose_name='Category Alias'),
        ),
    ]
