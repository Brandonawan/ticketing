# Generated by Django 4.2.15 on 2024-08-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Missing results'), ('2', 'Biodata update'), ('3', 'Assault')], max_length=255)),
                ('description', models.TextField()),
                ('upload', models.ImageField(upload_to='upload/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
