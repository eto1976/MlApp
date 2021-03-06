# Generated by Django 2.1.2 on 2019-09-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mst_imagelabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelclass', models.CharField(max_length=3)),
                ('labelclassname', models.CharField(max_length=100)),
                ('baselabelclass', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'mst_imagelabel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mst_user',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('mailaddress', models.CharField(max_length=40)),
                ('adminflg', models.CharField(max_length=1)),
                ('createdate', models.DateTimeField()),
                ('updatedate', models.DateTimeField()),
            ],
            options={
                'db_table': 'mst_user',
                'managed': False,
            },
        ),
    ]
