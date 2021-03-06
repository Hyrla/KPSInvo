# Generated by Django 3.1.2 on 2020-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_auto_20201015_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='food',
            name='price_cotisant',
            field=models.FloatField(default=0.9),
        ),
        migrations.AddField(
            model_name='foodsale',
            name='is_cotisant',
            field=models.BooleanField(default=False),
        ),
    ]
