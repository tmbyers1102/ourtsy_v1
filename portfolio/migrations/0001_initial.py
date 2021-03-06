# Generated by Django 3.1.4 on 2021-07-29 22:46

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
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.artist')),
            ],
        ),
        migrations.CreateModel(
            name='ArtItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.artist')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=models.ManyToManyField(blank=True, to='portfolio.Genres'),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
