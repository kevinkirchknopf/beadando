# Generated by Django 4.1.4 on 2022-12-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='Nincs kép!', upload_to='images'),
        ),
    ]