# Generated by Django 5.0.4 on 2024-05-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('poster', models.URLField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('genre', models.CharField(max_length=200)),
                ('video_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
