# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages

import csv


def square(request):
    data = []

    a = request.GET.get('a', None)
    if a is None or not a.isdigit() or a == '0':
        messages.error(request, 'Wrong a')
        return render(request, 'nine/square.html',)
    else:
        a = float(a)

    b = request.GET.get('b', None)
    if b is None or not b.isdigit():
        messages.error(request, 'Wrong b')
        return render(request, 'nine/square.html',)
    else:
        b = float(b)

    c = request.GET.get('c', None)
    if c is None or not c.isdigit():
        messages.error(request, 'Wrong c')
        return render(request, 'nine/square.html',)
    else:
        c = float(c)

    d = b ** 2 - 4 * a * c

    if d > 0:
        data.append((-b + d**(1/2)) / (2 * a))
        data.append((-b - d**(1/2)) / (2 * a))
    elif d == 0:
        data.append(-b / (2 * a))
    else:
        messages.info(request, 'Roots absent')

    return render(request, 'nine/square.html',
                  {"data": data,
                   })


def heroes(request):
    array_row = []
    with open('nine/data.csv', 'r') as fp:
        csv_r = csv.reader(fp)
        for row in csv_r:
            array_row.append(row)
    return render(request, 'nine/heroes.html',
                  {'titles': array_row[0],
                   'data': array_row[1::],
                   })

