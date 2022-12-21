# Generated by Django 4.1.4 on 2022-12-17 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('yosh', models.IntegerField()),
                ('ish_vaqti', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Haydovchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('kiritilgan_sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=50)),
                ('narx', models.IntegerField()),
                ('litr', models.CharField(max_length=50)),
                ('batafsil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=50)),
                ('qarz', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('miqdori', models.CharField(max_length=50)),
                ('narx', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.admin')),
                ('haydovchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.haydovchi')),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mijoz')),
                ('suv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.suv')),
            ],
        ),
    ]
