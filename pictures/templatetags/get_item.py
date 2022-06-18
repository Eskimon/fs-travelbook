from django import template

register = template.Library()


@register.simple_tag
def get_selected_item(dictionary, key, needle):
    dico = dict(dictionary).get(key)
    return "selected" if dico and (str(needle) in dico) else ""


@register.simple_tag
def encode_flights_item(dictionary):
    dico = dict(dictionary).get("flights", [])
    return "&".join([f"flights={f}" for f in dico]) if dico else ""
