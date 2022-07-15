# Generated by Django 3.2.9 on 2022-06-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAPIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
