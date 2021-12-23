from django import template

register = template.Library()

'''
this module is used to get filter in order
to parse dictionnary in the web page view
'''

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
