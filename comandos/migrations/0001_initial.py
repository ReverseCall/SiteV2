# Generated by Django 4.0.6 on 2023-11-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('dia_envio', models.DateField()),
                ('horario_envio', models.TimeField()),
                ('tipo_mensagem', models.CharField(choices=[('dica', 'Dica'), ('informacao', 'Informação')], default='informacao', max_length=20)),
                ('ultima', models.BooleanField(default=False)),
                ('mensagem_adicional', models.TextField(blank=True, null=True)),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='audios/')),
            ],
        ),
    ]
