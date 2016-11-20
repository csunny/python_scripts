#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author: magic
"""
from xml.etree.cElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BOOKs = {
    '0132269937': {
        'title': 'Core Python Program',
        'edition': 2,
        'year': 2006,
    },
    '0132356139': {
        'title': 'Python Web Development with Django',
        'author': 'Jeff Forcier',
        'year': 2009,
    },
    '0137143419': {
        'title': 'Python Fundamentals',
        'year': 2009,
    },
}

books = Element('books')
for isbn, info in BOOKs.iteritems():
    # print isbn, info
    book = SubElement(books, 'book')
    info.setdefault('author', 'Wesley Chun')
    info.setdefault('editor', 1)
    # print info
    for key, val in info.iteritems():
        SubElement(book, key).text = ', '.join(str(val) .split(':'))

xml = tostring(books)
dom = parseString(xml)
print dom.toprettyxml('    ')