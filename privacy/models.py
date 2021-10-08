from django.db import models
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel, StreamFieldPanel,RichTextField, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock


class PrivacyPage(Page):
    template = "privacy/privacy_page.html"

    page_title = models.CharField(max_length=255, null=True,blank=False)
    content = StreamField([
        ('Privacy',blocks.StructBlock([
            ("privacy_title", blocks.CharBlock()),
            ('privacy_second_title', blocks.CharBlock(required=False)),
            ('privacy_content',blocks.RichTextBlock())
        ]))
    ],null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        StreamFieldPanel("content"),
    ]