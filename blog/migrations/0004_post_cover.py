# Generated by Django 3.2.16 on 2023-03-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
