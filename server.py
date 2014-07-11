#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import sockgen


app = Flask(__name__)


@app.route('/')
def form():

    units = request.args.get('units', 'inches')

    try:
        stitches = float(request.args.get('stitches', 24))
        st_color = "#FFFFFF"
    except ValueError:
        stitches = 24
        st_color = "#FA5858"

    try:
        rows = float(request.args.get('rows', 30))
        r_color = "#FFFFFF"
    except ValueError:
        rows = 30
        r_color = "#FA5858"


    try:
        circum = float(request.args.get('circum', 7))
        c_color = "#FFFFFF"
    except ValueError:
        c_color = "#FA5858"
        circum = 7


    try:
        foot_length = float(request.args.get('foot_length', 8))
        fl_color = "#FFFFFF"
    except ValueError:
        fl_color = "#FA5858"
        foot_length = 8


    try:
        ease = float(request.args.get('ease', -8))
        e_color = "#FFFFFF"
    except ValueError:
        ease = -8
        e_color = "#FA5858"


    sock_info = sockgen.Pattern_info(units, stitches, rows)

    pattern = sockgen.pattern(sock_info, circum, foot_length)

    #if stitches == None or rows == None or circum == None or length == None:
    #    return "Parameters missing.  Enter values for units (optional, default " \
    #           "is inches), stitches, rows, circum, length, ease (optional, default is -8)."
    #else:
    result = render_template('form.html',
                             st_color=st_color, r_color=r_color, c_color=c_color, fl_color=fl_color, e_color=e_color,
                             units=units, stitches=stitches, rows=rows, circum=circum, foot_length=foot_length, ease=ease,
                             sock_info=sock_info,
                             cast_on = pattern[0],
                             heel_end = pattern[1],
                             toe_end = pattern[2],
                             heel_length = pattern[3],
                             )
    return result

@app.route('/links')
def links():
    return render_template('links.html', links = True)

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
