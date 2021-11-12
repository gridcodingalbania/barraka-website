from django.db import models
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel,RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class WhatWeCanDo(Page):

    template = "whatwecando/whatwecando_page.html"

    page_title = models.CharField(max_length=200, null=True, blank=True)
    page_subtitle = models.CharField(max_length=200, null=True, blank=True)
    
    page_second_title = models.CharField(max_length=200, null=True, blank=True)

    cards_content = StreamField([
    ('cards', blocks.StructBlock([
        ('cards_image', ImageChooserBlock(required=False)),
        ('cards_title', blocks.CharBlock()),
        ('cards_description', blocks.RichTextBlock()),
    ]))
    ],null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("page_subtitle"),
        FieldPanel("page_second_title"),
        StreamFieldPanel("cards_content"),
    ]