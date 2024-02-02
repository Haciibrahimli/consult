from modeltranslation.translator import TranslationOptions, register
from my_app.models import Service, Quota, Blog, Team, Testimonial, AboutModel
                          

@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ("title","description", )

@register(Quota)
class QuotaTranslation(TranslationOptions):
    fields = ("name","service", )

@register(Blog)
class BlogTranslation(TranslationOptions):
    fields = (
        "title",
        "description",
      
    )

@register(Team)
class TeamTranslation(TranslationOptions):
    fields = ("name","position" )

@register(Testimonial)
class TestimonialTranslation(TranslationOptions):
    fields = ("description", "profesion")


@register(AboutModel)
class AboutModelTranslation(TranslationOptions):
    fields = ("description", "title", "sub_title")

