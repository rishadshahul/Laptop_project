# Generated by Django 4.2 on 2023-05-17 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModernApp', '0005_productdb_procate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productDB',
            new_name='productDB2',
        ),
        migrations.RenameField(
            model_name='productdb2',
            old_name='Procate',
            new_name='ProductCategory',
        ),
    ]