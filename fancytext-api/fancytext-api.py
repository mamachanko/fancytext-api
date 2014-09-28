# -*- coding: utf-8 -*-

from bottle import route, run, request
from fancytext import fancy


@route('/fancy', method='POST')
def fancify():
    plain_text = request.POST['text']
    return fancy(plain_text)

run(host='localhost', port=8080)
