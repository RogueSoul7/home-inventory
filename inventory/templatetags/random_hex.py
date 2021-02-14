import random
from django import template

register = template.Library()


@register.simple_tag
def random_hex_color():
  random_number = random.randint(0, 16777215)
  hex_number = str(hex(random_number))
  hex_number = '#' + hex_number[2:]
  return hex_number
