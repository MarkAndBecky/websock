#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from urllib import urlencode

import sockgen


app = Flask(__name__)

def form_input(request):

    units = request.args.get('units', 'inches')
    error = False

    try:
        stitches = float(request.args.get('stitches', 24))
        st_color = "#FFFFFF"
    except ValueError:
        stitches = request.args.get('stitches')
        st_color = "#FA5858"
        error = True

    try:
        rows = float(request.args.get('rows', 30))
        r_color = "#FFFFFF"
    except ValueError:
        rows = request.args.get('rows')
        r_color = "#FA5858"
        error = True

    try:
        circum = float(request.args.get('circum', 7))
        c_color = "#FFFFFF"
    except ValueError:
        c_color = "#FA5858"
        circum = request.args.get('circum')
        error = True

    try:
        foot_length = float(request.args.get('foot_length', 8))
        fl_color = "#FFFFFF"
    except ValueError:
        fl_color = "#FA5858"
        foot_length = request.args.get('foot_length')
        error = True

    try:
        ease = float(request.args.get('ease', -8))
        e_color = "#FFFFFF"
    except ValueError:
        ease = request.args.get('ease')
        e_color = "#FA5858"
        error = True

    result = [st_color, r_color, c_color, fl_color, e_color, units, stitches, rows, circum, foot_length, ease, error]
    return result


@app.route('/')
def form():

    input_fields = form_input(request)

    result = render_template('form.html', st_color=input_fields[0], r_color=input_fields[1], c_color=input_fields[2],
                             fl_color=input_fields[3], e_color=input_fields[4], units=input_fields[5],
                             stitches=input_fields[6], rows=input_fields[7], circum=input_fields[8],
                             foot_length=input_fields[9], ease=input_fields[10],)

    return result

@app.route('/links')
def links():
    return render_template('links.html')


@app.route('/pattern')
def pattern():

    input_fields = form_input(request)
    units = input_fields[5]
    stitches = input_fields[6]
    rows = input_fields[7]
    circum = input_fields[8]
    foot_length = input_fields[9]
    ease = input_fields[10]
    error = input_fields[11]

    if error == True:
        url_values = {'units' : units,
            'stitches' : stitches,
            'rows' : rows,
            'circum' : circum,
            'foot_length' : foot_length,
            'ease' : ease}

        url = '/?' + urlencode(url_values)

        result = redirect(url)

    else:

        sock_info = sockgen.Pattern_info(units, stitches, rows)

        pattern = sockgen.pattern(sock_info, circum, foot_length)

        result = render_template('pattern.html',
                                 st_color=input_fields[0], r_color=input_fields[1], c_color=input_fields[2],
                                 fl_color=input_fields[3], e_color=input_fields[4],
                                 units=units, stitches=stitches, rows=rows, circum=circum, foot_length=foot_length, ease=ease,
                                 sock_info=sock_info,
                                 cast_on = pattern[0],
                                 heel_end = pattern[1],
                                 toe_end = pattern[2],
                                 heel_length = pattern[3],
                                 )
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
