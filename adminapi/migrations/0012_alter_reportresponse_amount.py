# Generated by Django 4.2.5 on 2024-03-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0011_alter_reportresponse_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportresponse',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
