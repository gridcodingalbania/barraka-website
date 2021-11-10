from django.db import models
from django.db.models.fields import Field
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel,RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class ShowreelListingPage(Page):
    tempalte = "showreel/showreel_listing_page.html"

    listing_title = models.CharField(max_length=200, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("listing_title"),
    ]

class ShowreelDetailPage(Page):
    template = "showreel/showreel_detail_page.html"

    detail_title = models.CharField(max_length=200, null=True, blank=True)
    detail_subtitle = models.CharField(max_length=200, null=True, blank=True)
    detail_description = RichTextField(null=True, blank=False)

    
    detail_content = StreamField([
    ('Detail', blocks.StructBlock([
        ('detail_video_id',blocks.CharBlock()),
        ('detail_video_target',blocks.CharBlock()),
        ('detail_video_image', ImageChooserBlock(required=False)),
        ('detail_video_link', blocks.CharBlock()),
        ('detail_video_title',blocks.CharBlock()),

    ]))
    ],null=True,blank=False)


    content_panels = Page.content_panels + [
        FieldPanel("detail_title"),
        FieldPanel("detail_subtitle"),
        FieldPanel("detail_description"),
        StreamFieldPanel("detail_content"),
    ]