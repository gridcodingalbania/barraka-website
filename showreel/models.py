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

    detail_big_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    
    big_image_id = models.CharField(max_length=200,null=True,blank=True)
    detail_big_image_video_target = models.CharField(max_length=200,null=True,blank=True)
    detail_big_image_video_link = models.CharField(max_length=1000,null=True,blank=True)
    detail_big_image_title = models.CharField(max_length=200, null=True, blank=True)
    detail_big_image_description = RichTextField(blank=False, null=True)
    
    detail_content = StreamField([
    ('Detail', blocks.StructBlock([
        ('detail_video_id',blocks.CharBlock()),
        ('detail_video_target',blocks.CharBlock()),
        ('detail_video_image', ImageChooserBlock(required=False)),
        ('detail_video_link', blocks.CharBlock()),
        ('detail_video_title',blocks.CharBlock()),
        ('detail_video_description',blocks.RichTextBlock()),
    ]))
    ],null=True,blank=False)


    content_panels = Page.content_panels + [
        FieldPanel("detail_title"),
        FieldPanel("detail_subtitle"),
        FieldPanel("detail_description"),
        ImageChooserPanel("detail_big_image"),
        FieldPanel("big_image_id"),
        FieldPanel("detail_big_image_video_target"),
        FieldPanel("detail_big_image_video_link"),
        FieldPanel("detail_big_image_title"),
        FieldPanel("detail_big_image_description"),
        StreamFieldPanel("detail_content"),
    ]