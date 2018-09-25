# Generated by Django 2.0.8 on 2018-09-24 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("concordia", "0022_auto_20180924_1511")]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="concordia.Item"
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="concordia.Project"
            ),
        ),
    ]
