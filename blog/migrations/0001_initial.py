# Generated by Django 4.1.7 on 2023-06-10 22:22

import blog.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='Krótka informacja o autorze, maksymalnie 512 znaków.', validators=[blog.models.validate_bio], verbose_name='O autorze')),
                ('profile_pic', models.ImageField(upload_to='images/profile/', verbose_name='Zdjęcie profilowe')),
                ('author_quote', models.TextField(help_text='Krótkie motto autora, maksymalnie 128 znaków.', validators=[blog.models.validate_author_quote], verbose_name='Cytat autora')),
                ('author_function', models.TextField(help_text='Nazwa funkcji jaką pełni autor.', validators=[blog.models.validate_author_function], verbose_name='Stanowisko autora')),
                ('author_url', models.URLField(blank=True, null=True, verbose_name='URL do strony użytkowanika')),
                ('pinterest_url', models.URLField(blank=True, null=True, validators=[blog.models.validate_pinterest], verbose_name='URL do Pinteresta')),
                ('facebook_url', models.URLField(blank=True, null=True, validators=[blog.models.validate_facebook], verbose_name='URL do Facebooka')),
                ('twitter_url', models.URLField(blank=True, null=True, validators=[blog.models.validate_twitter], verbose_name='URL do Twittera')),
                ('instagram_url', models.URLField(blank=True, null=True, validators=[blog.models.validate_instagram], verbose_name='URL do Instagrama')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(validators=[blog.models.validate_title], verbose_name='Tytuł')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Treść')),
                ('introduction', models.TextField(null=True, validators=[blog.models.validate_introduction], verbose_name='Wstęp')),
                ('background', models.ImageField(upload_to='images/post/', verbose_name='Tło wpisu')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='Data publikacji')),
                ('date_edited', models.DateTimeField(auto_now=True, verbose_name='Data ostatniej edycji')),
                ('favorite', models.BooleanField(default=False, verbose_name='Czy wyróżnić post?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Kategoria o tej nazwie już istnieje'}, max_length=128, unique=True, validators=[blog.models.validate_category], verbose_name='Kategoria')),
                ('description', models.TextField(max_length=512, validators=[blog.models.validate_category_description], verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Krótka informacja o użytkowniku, maksymalnie 512 znaków.', validators=[blog.models.validate_bio], verbose_name='Bio')),
                ('profile_pic', models.ImageField(default='images/profile/1.png', upload_to='images/user/', verbose_name='Zdjęcie profilowe')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='PL', unique=True, verbose_name='Numer telefonu')),
                ('gender', models.CharField(choices=[('M', 'Mężczyzna'), ('K', 'Kobieta'), ('I', 'Inna')], default='Mężczyzna', max_length=6, verbose_name='Płeć')),
                ('Newsletter', models.BooleanField(default=False, verbose_name='Biuletyn')),
                ('miss_news', models.BooleanField(default=False, verbose_name='Pominięte artykuły')),
                ('meetups_news', models.BooleanField(default=True, verbose_name='Spotkania i wydarzenia')),
                ('opportunities_news', models.BooleanField(default=False, verbose_name='Okazje z rynku aukcyjnego')),
                ('company_news', models.BooleanField(default=True, verbose_name='Wiadomości od Banknoty')),
                ('replay_news', models.BooleanField(default=False, verbose_name='Shot wydzarzeń na Banknoty')),
                ('development_news', models.BooleanField(default=False, verbose_name='Informacje o rozwoju i zmianach na Banknoty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Tytuł')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Treść')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('status_field', models.CharField(choices=[('Draft', 'Projekt'), ('Published', 'Opublikowany')], default='Draft', max_length=10)),
                ('email', models.ManyToManyField(to='blog.newsletteruser', verbose_name='Subskrybujący')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(validators=[blog.models.validate_content], verbose_name='Komentarz')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='Data publikacji')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='Wpis')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(help_text='Wyświetlą się maksymalnie trzy kategorie', max_length=256, to='blog.category', verbose_name='Kategorie'),
        ),
    ]
