# Generated by Django 3.1.2 on 2020-10-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20201020_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ID',
        ),
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]