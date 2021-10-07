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

    homePage_second_Title = models.CharField(max_length=200, null=True, blank=True)
    homePage_second_subTitle = models.CharField(max_length=200,null=True,blank=True)
 
    reel_content = StreamField([
    ('Reels', blocks.StructBlock([
        ('reel_video_id', blocks.CharBlock()),
        ('reel_video_target', blocks.CharBlock()),
        ('reel_video_image', ImageChooserBlock(required=False)),
        ('reel_video_link', blocks.CharBlock()),
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

    reels_big_video_id = models.CharField(max_length=200,null=True,blank=True)
    reels_big_video_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    reels_big_video_target = models.CharField(max_length=200,null=True,blank=True)
    reels_big_video_link = models.CharField(max_length=1000,null=True,blank=True)

    portfolio_content = StreamField([
    ('Portfolio', blocks.StructBlock([
        ('portfolio_video_id',blocks.CharBlock()),
        ('portfolio_video_target',blocks.CharBlock()),
        ('portfolio_video_image', ImageChooserBlock(required=False)),
        ('portfolio_video_link', blocks.CharBlock()),
        ('portfolio_video_title',blocks.CharBlock()),
        ('portfolio_video_description',blocks.RichTextBlock()),
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

    content_panels = Page.content_panels + [
        FieldPanel("banner_text"),
        FieldPanel("colored_banner_text"),
        FieldPanel("banner_text_after_colored"),
        FieldPanel("homePage_first_Title"),
        FieldPanel("homePage_first_subTitle"),
        FieldPanel("homePage_first_description"),
        ImageChooserPanel("homePage_first_Image"),
        FieldPanel("homePage_second_Title"),
        FieldPanel("homePage_second_subTitle"),
        FieldPanel("reels_big_video_id"),
        ImageChooserPanel("reels_big_video_image"),
        FieldPanel("reels_big_video_target"),
        FieldPanel("reels_big_video_link"),
        StreamFieldPanel("reel_content"),
        FieldPanel("homePage_third_Title"),
        FieldPanel("homePage_third_subTitle"),
        FieldPanel("homePage_third_description"),
        ImageChooserPanel("homePage_third_Image"),
        StreamFieldPanel("portfolio_content"),
        FieldPanel("homePage_fourth_Title"),
        FieldPanel("homePage_fourth_subTitle"),
        FieldPanel("homePage_fourth_description"),
        ImageChooserPanel("homePage_fourth_Image"),
    ]