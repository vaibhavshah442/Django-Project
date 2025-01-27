# Generated by Django 4.0.5 on 2022-07-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pylib', '0006_alter_book_file_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='bookpdf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(unique=True),
        ),
    ]
