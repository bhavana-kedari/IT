# Generated by Django 5.0.3 on 2024-03-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_remove_category_num_likes_remove_category_num_visits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='num_visits',
            field=models.IntegerField(default=0),
        ),
    ]