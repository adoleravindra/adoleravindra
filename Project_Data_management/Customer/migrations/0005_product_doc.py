# Generated by Django 2.2.6 on 2019-11-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_auto_20191127_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='doc',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]