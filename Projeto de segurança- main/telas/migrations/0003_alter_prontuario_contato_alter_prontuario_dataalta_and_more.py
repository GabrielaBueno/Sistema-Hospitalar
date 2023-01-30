# Generated by Django 4.1.4 on 2022-12-11 19:05

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telas', '0002_alter_prontuario_medicacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prontuario',
            name='contato',
            field=fernet_fields.fields.EncryptedCharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dataAlta',
            field=fernet_fields.fields.EncryptedDateField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dataInternacao',
            field=fernet_fields.fields.EncryptedDateField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dataNascimento',
            field=fernet_fields.fields.EncryptedDateField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='medicacao',
            field=fernet_fields.fields.EncryptedTextField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='nRegistro',
            field=fernet_fields.fields.EncryptedCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='nome',
            field=fernet_fields.fields.EncryptedCharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='observacoesComplementares',
            field=fernet_fields.fields.EncryptedTextField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='pressaoArterial',
            field=fernet_fields.fields.EncryptedCharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='principaisSintomas',
            field=fernet_fields.fields.EncryptedTextField(),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='temperatura',
            field=fernet_fields.fields.EncryptedCharField(max_length=10),
        ),
    ]
