# Generated by Django 4.1.6 on 2023-02-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='static/products/')),
            ],
        ),
    ]
