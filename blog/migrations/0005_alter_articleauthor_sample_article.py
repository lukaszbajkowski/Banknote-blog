# Generated by Django 4.1.7 on 2023-06-19 07:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_articleauthor_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleauthor',
            name='sample_article',
            field=ckeditor.fields.RichTextField(verbose_name='Próbny artykuł'),
        ),
    ]
