# Generated by Django 4.2.1 on 2023-08-31 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('masv', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('hotensv', models.CharField(max_length=30)),
                ('lophocphan', models.CharField(max_length=10)),
                ('ngaysinh', models.DateField()),
                ('ghichu', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('gvcn', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('hotensv', models.CharField(max_length=30)),
                ('lophocphan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sinhvien')),
            ],
        ),
    ]