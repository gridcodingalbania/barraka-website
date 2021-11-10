from django.db import models
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel,RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):

    template = "home/home_page.html"

    banner_text = models.CharField(max_length=200, null=True, blank=True)
    colored_banner_text = models.CharField(max_length=200, null=True, blank=True)
    banner_text_after_colored = models.CharField(max_length=200, null=True, blank=True)

    homePage_first_Title = models.CharField(max_length=200, null=True, blank=True)
    homePage_first_subTitle = models.CharField(max_length=200,null=True,blank=True)
    homePage_first_description = RichTextField(null=True, blank=False)
    homePage_first_Image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    homePage_services_title = models.CharField(max_length=200, null=True, blank=True)
    homePage_services_subTitle = models.CharField(max_length=200, null=True, blank=True)
    homePage_services_content = StreamField([
    ('Card', blocks.StructBlock([
        ('card_image', ImageChooserBlock(required=False)),
        ('card_title',blocks.CharBlock()),
    ]))
    ],null=True,blank=False)

    homePage_third_Title = models.CharField(max_length=200, null=True, blank=True)
    homePage_third_subTitle = models.CharField(max_length=200,null=True,blank=True)
    homePage_third_description = RichTextField(null=True, blank=False)
    homePage_third_Image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )


    reels_content = StreamField([
    ('Reels', blocks.StructBlock([
        ('reel_image', ImageChooserBlock(required=False)),
        ('reel_link', blocks.CharBlock()),
        ('reel_title',blocks.CharBlock()),
    ]))
    ],null=True,blank=False)

    homePage_fourth_Title = models.CharField(max_length=200, null=True, blank=True)
    homePage_fourth_subTitle = models.CharField(max_length=200,null=True,blank=True)
    homePage_fourth_description = RichTextField(null=True, blank=False)
    homePage_fourth_Image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
 

   

    homePage_partners_title = models.CharField(max_length=200, null=True, blank=True)
    homePage_partners_subtitle = models.CharField(max_length=200, null=True, blank=True)
    homePage_partners_description = RichTextField(null=True, blank=False)

    partners_content = StreamField([
    ('Partners', blocks.StructBlock([
        ('partners_logo', ImageChooserBlock(required=False)),
    ]))
    ],null=True,blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("banner_text"),
        FieldPanel("colored_banner_text"),
        FieldPanel("banner_text_after_colored"),
        FieldPanel("homePage_first_Title"),
        FieldPanel("homePage_first_subTitle"),
        FieldPanel("homePage_first_description"),
        ImageChooserPanel("homePage_first_Image"),
        FieldPanel("homePage_services_title"),
        FieldPanel("homePage_services_subTitle"),
        StreamFieldPanel("homePage_services_content"),
        FieldPanel("homePage_third_Title"),
        FieldPanel("homePage_third_subTitle"),
        FieldPanel("homePage_third_description"),
        ImageChooserPanel("homePage_third_Image"),
        StreamFieldPanel("reels_content"),
        FieldPanel("homePage_fourth_Title"),
        FieldPanel("homePage_fourth_subTitle"),
        FieldPanel("homePage_fourth_description"),
        ImageChooserPanel("homePage_fourth_Image"),
        FieldPanel("homePage_partners_title"),
        FieldPanel("homePage_partners_subtitle"),
        FieldPanel("homePage_partners_description"),
        StreamFieldPanel("partners_content"),
    ]