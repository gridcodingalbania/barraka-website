# Generated by Django 3.2.5 on 2021-09-28 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0007_auto_20210927_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='reels_big_video_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='reels_big_video_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='reels_big_video_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='reels_big_video_target',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
