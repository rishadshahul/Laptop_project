# Generated by Django 4.2 on 2023-05-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModernApp', '0002_remove_categorydb_cateimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydb',
            name='cateImage',
            field=models.ImageField(default=123, upload_to='profile'),
            preserve_default=False,
        ),
    ]
