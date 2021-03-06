# Generated by Django 3.0.7 on 2020-11-18 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('world', 'World'), ('environment', 'Environment'), ('technical', 'Technical'), ('design', 'Design'), ('culture', 'Culture'), ('politics', 'Politics'), ('business', 'Business'), ('work', 'Work'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('travel', 'Travel')], default='business', max_length=50)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('excerpt', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
