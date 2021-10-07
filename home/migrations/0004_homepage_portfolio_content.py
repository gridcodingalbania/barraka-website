# Generated by Django 3.2.5 on 2021-09-27 13:29

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210927_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='portfolio_content',
            field=wagtail.core.fields.StreamField([('Portfolio', wagtail.core.blocks.StructBlock([('portfolio_video_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('portfolio_video_link', wagtail.core.blocks.CharBlock()), ('portfolio_video_title', wagtail.core.blocks.CharBlock()), ('portfolio_video_description', wagtail.core.blocks.RichTextBlock())]))], null=True),
        ),
    ]