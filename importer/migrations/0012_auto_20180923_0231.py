# Generated by Django 2.0.8 on 2018-09-23 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0011_auto_20180922_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importitem',
            name='status',
            field=models.TextField(blank=True, default='', verbose_name='Status message, if any, from the last worker'),
        ),
        migrations.AlterField(
            model_name='importitemasset',
            name='status',
            field=models.TextField(blank=True, default='', verbose_name='Status message, if any, from the last worker'),
        ),
        migrations.AlterField(
            model_name='importjob',
            name='status',
            field=models.TextField(blank=True, default='', verbose_name='Status message, if any, from the last worker'),
        ),
    ]
