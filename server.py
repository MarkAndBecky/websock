#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import sockgen


app = Flask(__name__)


@app.route('/')
def form():


    result = render_template('form.html',
                             st_color="#FFFFFF", r_color="#FFFFFF", c_color="#FFFFFF", fl_color="#FFFFFF", e_color="#FFFFFF",
                             units='inches', stitches=24, rows=30, circum=7, foot_length=8, ease=-8,
                             )
    return result

@app.route('/links')
def links():
    return render_template('links.html')


@app.route('/pattern')


def pattern():

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

    #if request.form['reset']:
    #    result = render_template('form.html',
    #                         st_color="#FFFFFF", r_color="#FFFFFF", c_color="#FFFFFF", fl_color="#FFFFFF", e_color="#FFFFFF",
    #                         units='inches', stitches=24, rows=30, circum=7, foot_length=8, ease=-8,
    #                         )

    if error == True:

        result = render_template('form.html',
                                 st_color=st_color, r_color=r_color, c_color=c_color, fl_color=fl_color, e_color=e_color,
                                 units=units, stitches=stitches, rows=rows, circum=circum, foot_length=foot_length, ease=ease,)
    else:

        sock_info = sockgen.Pattern_info(units, stitches, rows)

        pattern = sockgen.pattern(sock_info, circum, foot_length)

        result = render_template('pattern.html',
                                 st_color=st_color, r_color=r_color, c_color=c_color, fl_color=fl_color, e_color=e_color,
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
