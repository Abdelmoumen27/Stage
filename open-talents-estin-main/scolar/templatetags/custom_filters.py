from django import template 
import json


register = template.Library()
@register.filter
def get_range(value):
    return range(value)


@register.filter
def get_value(dict, key):
    # print(key)
    key1, key2 = key.split(',')
    item = dict.get(key1, None)
    if item is None:
        return None
    item = item.get(key2, None)
    if item is None:
        return None
    return item

# @register.filter
# def json_list(objects):
#     ids = [object.id for object in objects]
#     return json.dumps(ids)

@register.filter
def printer(value):
    print(value)


from datetime import datetime

@register.filter
def get_day_name(dayFormat):
    day = datetime.strptime(dayFormat, '%Y-%m-%d')
    return day.strftime('%A')