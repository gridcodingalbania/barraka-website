# Generated by Django 3.2.8 on 2021-11-10 12:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211110_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='portfolio_content',
        ),
        migrations.AddField(
            model_name='homepage',
            name='reels_content',
            field=wagtail.core.fields.StreamField([('Reels', wagtail.core.blocks.StructBlock([('reel_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('reel_link', wagtail.core.blocks.CharBlock()), ('reel_title', wagtail.core.blocks.CharBlock())]))], null=True),
        ),
    ]
