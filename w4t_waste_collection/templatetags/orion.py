from django import template

register = template.Library()


@register.simple_tag
def orion_display(orion_element, cotainer='div'):
    snippet = "<"+cotainer+">"
    return orion_element.get("value")
