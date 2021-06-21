# Generated by Django 3.1.2 on 2021-06-18 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskProject', '0008_auto_20210613_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='horario_previsao_termino',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='quadro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='taskProject.quadro'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_previsao_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]