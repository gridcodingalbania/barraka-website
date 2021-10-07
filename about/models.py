from django.db import models
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel,RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class AboutPage(Page):

    template = "about/about_page.html"

    about_title = models.CharField(max_length=200, null=True, blank=True)
    about_subtitle = models.CharField(max_length=200, null=True, blank=True)

    first_about_title = models.CharField(max_length=200, null=True, blank=True)
    first_about_description = RichTextField(null=True, blank=False)
    first_about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    second_about_title = models.CharField(max_length=200, null=True, blank=True)
    second_about_subtitle = models.CharField(max_length=200, null=True, blank=True)
    second_about_description = RichTextField(null=True, blank=False)

    services_content = StreamField([
    ('services', blocks.StructBlock([
        ('service_image', ImageChooserBlock(required=False)),
        ('service_title', blocks.CharBlock()),
        ('service_description', blocks.RichTextBlock()),
    ]))
    ],null=True,blank=False)

    third_about_title = models.CharField(max_length=200, null=True, blank=True)

    other_services_content = StreamField([
    ('other_services', blocks.StructBlock([
        ('service_image', ImageChooserBlock(required=False)),
        ('service_title', blocks.CharBlock()),
        ('service_description', blocks.RichTextBlock()),
    ]))
    ],null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("about_title"),
        FieldPanel("about_subtitle"),
        FieldPanel("first_about_title"),
        FieldPanel("first_about_description"),
        ImageChooserPanel("first_about_image"),
        FieldPanel("second_about_title"),
        FieldPanel("second_about_subtitle"),
        FieldPanel("second_about_description"),
        StreamFieldPanel("services_content"),
        FieldPanel("third_about_title"),
        StreamFieldPanel("other_services_content"),
    ]