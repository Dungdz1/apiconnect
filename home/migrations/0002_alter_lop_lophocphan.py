# Generated by Django 4.2.1 on 2023-09-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lop',
            name='lophocphan',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
