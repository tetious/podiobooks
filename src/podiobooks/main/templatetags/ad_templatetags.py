""" Django Custom Template Tags for Advertising-Related Stuff """

from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('main/ad/tags/ad_placeholder.html')
def ad_placeholder():
    """Placeholder for Future Ads"""
    return {'MEDIA_URL': settings.MEDIA_URL}
