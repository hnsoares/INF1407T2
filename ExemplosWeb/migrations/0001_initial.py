# Generated by Django 3.2.16 on 2022-11-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre o nome', max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, help_text='Entre o preço', max_digits=8)),
                ('qtd', models.IntegerField(help_text='Entre a quantidade')),
            ],
        ),
    ]
