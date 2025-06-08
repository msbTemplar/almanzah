import re
from django import template

register = template.Library()

@register.filter
def digits_only(value):
    return re.sub(r'\D', '', str(value))  # elimina todo lo que no sea dígito
