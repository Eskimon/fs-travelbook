import re

from django import template

try:
    from django.urls import NoReverseMatch, reverse
except ImportError:
    from django.core.urlresolvers import NoReverseMatch, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = "^" + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context["request"].path
    if re.search(pattern, path):
        return "is-active"
    return ""
