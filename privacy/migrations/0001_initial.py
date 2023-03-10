# Generated by Django 3.2.5 on 2021-10-08 08:37

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title', models.CharField(max_length=255, null=True)),
                ('content', wagtail.core.fields.StreamField([('Privacy', wagtail.core.blocks.StructBlock([('privacy_title', wagtail.core.blocks.CharBlock()), ('privacy_second_title', wagtail.core.blocks.CharBlock(required=False)), ('privacy_content', wagtail.core.blocks.RichTextBlock())]))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
