# Generated by Django 5.1.2 on 2024-11-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
            ],
        ),
    ]