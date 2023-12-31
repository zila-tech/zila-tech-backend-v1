# Generated by Django 4.1.6 on 2023-10-02 17:39

import api_portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_portfolio', '0003_experience_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirmLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to=api_portfolio.models.upload_to)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('use', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='wrapperimage',
            name='bgImg',
            field=models.ImageField(upload_to=api_portfolio.models.upload_to, verbose_name='Big Image'),
        ),
        migrations.AlterField(
            model_name='wrapperimage',
            name='mdImg',
            field=models.ImageField(upload_to=api_portfolio.models.upload_to, verbose_name='Normal Image'),
        ),
        migrations.AlterField(
            model_name='wrapperimage',
            name='smImg',
            field=models.ImageField(upload_to=api_portfolio.models.upload_to, verbose_name='Small Image'),
        ),
    ]
