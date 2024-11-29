from django import template

register = template.Library()

@register.filter
def range_filter(n):
    return range(1, n + 1)

@register.simple_tag
def get_attr(instance, field_name):
    return getattr(instance, field_name)


@register.simple_tag
def get_dynamic_attr(instance, attr_name):
    return getattr(instance, attr_name, None)
