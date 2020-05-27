# Generated by Django 3.0.3 on 2020-02-25 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectClassModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='static/data')),
                ('file_path', models.FileField(upload_to='static/data')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ObjectClassModel')),
            ],
        ),
    ]
