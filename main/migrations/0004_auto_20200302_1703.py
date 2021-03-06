# Generated by Django 3.0.3 on 2020-03-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200227_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='DontFakeMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='annotationimagemodel',
            name='annotate',
            field=models.FileField(upload_to='darknet/data/custom'),
        ),
        migrations.AlterField(
            model_name='annotationimagemodel',
            name='image',
            field=models.FileField(upload_to='darknet/data/custom'),
        ),
    ]
