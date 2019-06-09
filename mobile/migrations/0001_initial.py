# Generated by Django 2.1 on 2019-06-09 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(null=True)),
                ('moves', models.IntegerField(null=True)),
                ('result', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('access_token', models.CharField(max_length=50, null=True)),
                ('expires_time', models.IntegerField(null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('figureurl', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.User'),
        ),
    ]
