# Generated by Django 2.2.24 on 2021-06-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskProject', '0011_tarefa_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('senha', models.CharField(max_length=16)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]