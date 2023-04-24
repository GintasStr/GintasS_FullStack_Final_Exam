# Generated by Django 4.2 on 2023-04-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mk', '0005_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
