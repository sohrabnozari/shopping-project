# Generated by Django 3.2.8 on 2021-10-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_data_review_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='descriprion',
            new_name='descriprtion',
        ),
    ]
