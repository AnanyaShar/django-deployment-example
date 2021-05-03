## First register custom template
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of args from string!
    """

    return value.replace(arg,'')

## Register the custom Template
# register.filter('cut', cut)
