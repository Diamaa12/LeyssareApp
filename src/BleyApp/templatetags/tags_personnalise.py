from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value):
    return value

@register.filter(name='urls_recup')
def urls_recup(value, urls):
    value = urls
    return value