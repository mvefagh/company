# Generated by Django 3.2.9 on 2021-11-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('tech', 'Tech Business'), ('food', 'Food Industry')], default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='', verbose_name='Beschreibung der Firma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='number_of_employees',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='slogan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
