# Generated by Django 4.0.6 on 2022-07-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_transacao_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='tipo',
            field=models.CharField(choices=[('R', 'Receita'), ('D', 'Despesa')], default='D', max_length=1),
        ),
    ]
