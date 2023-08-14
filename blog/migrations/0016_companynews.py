# Generated by Django 4.1.7 on 2023-07-22 21:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auctionopportunities'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Tytuł')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Treść')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('status_field', models.CharField(choices=[('Draft', 'Projekt'), ('Published', 'Opublikowany')], default='Draft', max_length=10)),
            ],
        ),
    ]
