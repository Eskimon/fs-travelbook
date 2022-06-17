from django import template

register = template.Library()


@register.simple_tag
def get_selected_item(dictionary, key, needle):
    dico = dict(dictionary).get(key)
    return "selected" if str(needle) in dico else ""
