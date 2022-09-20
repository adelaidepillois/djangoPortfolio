#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: baptiste
# @Date:   2015-06-10 14:54:13
# @Last Modified by:   Baptiste
# @Last Modified time: 2017-10-25 16:26:34

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
import json
register = template.Library()
register.assignment_tag = register.simple_tag


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='addstr')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter(name='getpercent')
def getpercent(position, total):
    print("I CALCULATE PERCENT")
    print(position)
    print(total)
    return (position * 100) / total

@register.filter(name='addplaceholder')
def addplaceholder(field, placeholder):
    if field.field.required is True:
        placeholder = placeholder+" *"
    field.field.widget.attrs.update({"placeholder": placeholder})
    return field


@register.filter(name='get_percent')
def get_percent(price, init_price):
    if init_price and price and price < init_price:
        max_per = round(100 - (price * 100 / init_price))
        return 'Prix en baisse de ' + str(max_per) + ' %'
    return ''


@register.simple_tag
def active_tag(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.filter(name='join_tags')
def join_tags(tags):
    if not tags:
        return '(no tags)'
    elif len(tags) == 1:
        return tags[0]
    else:
        return ', '.join(tags[:-1]) + ' and ' + tags[-1]


@register.assignment_tag
def set(var):
    return var


@register.filter(name='to_class_name')
def to_class_name(value):
    return value.__class__.__name__


@register.filter(name='request_get_list')
def request_get_list(dict, name):
    return dict.getlist(name)


@register.filter(name='string_to_list')
def string_to_list(value):
    return value.split(",")


@register.filter(name='prepend_dollars')
def prepend_dollars(dollars):
    if dollars:
        dollars = round(float(dollars), 2)
        return "%s €" % (intcomma(int(dollars)))
    else:
        return ''
