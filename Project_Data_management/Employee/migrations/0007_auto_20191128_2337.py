# Generated by Django 2.2.6 on 2019-11-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_production_testing_quality_soldering_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_testing',
            name='ComBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='production_testing',
            name='RecBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='production_testing',
            name='RewBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='production_testing',
            name='TargetQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='production_testing',
            name='TestBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='ComBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='RecBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='RewBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='TargetQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='TestBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='soldering',
            name='ComBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='soldering',
            name='RewBorQty',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='soldering',
            name='TargetQty',
            field=models.IntegerField(max_length=1000),
        ),
    ]
