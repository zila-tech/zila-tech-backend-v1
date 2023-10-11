# Generated by Django 4.1.6 on 2023-10-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallary',
            options={'verbose_name': 'Gallary', 'verbose_name_plural': 'Gallary'},
        ),
        migrations.AddField(
            model_name='abouts',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='brands',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(default='Zilla Tech: Where Innovation Meets Success. Join us on the journey!', verbose_name='nate'),
        ),
        migrations.AddField(
            model_name='skills',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='work',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='use',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='wrapperimage',
            name='use',
            field=models.BooleanField(default=True),
        ),
    ]
