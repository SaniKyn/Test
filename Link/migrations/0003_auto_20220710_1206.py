# Generated by Django 3.2.14 on 2022-07-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Link', '0002_auto_20220710_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=256)),
                ('hash', models.CharField(db_index=True, max_length=10, unique=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
