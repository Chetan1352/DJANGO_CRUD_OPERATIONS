# Generated by Django 5.1.3 on 2024-12-03 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
