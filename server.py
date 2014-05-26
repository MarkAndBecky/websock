#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import sockgen


app = Flask(__name__)


@app.route('/')
def form():

    units = request.args.get('units', 'inches')
    #if units is None:
    #    units = "inch"

    stitches = float(request.args.get('stitches', 24))

    rows = float(request.args.get('rows', 30))

    circum = float(request.args.get('circum', 7))

    foot_length = float(request.args.get('foot_length', 8))

    ease = float(request.args.get('ease', -8))

    sock_info = sockgen.Pattern_info(units, stitches, rows)

    pattern = sockgen.pattern(sock_info, circum, foot_length)

    #if stitches == None or rows == None or circum == None or length == None:
    #    return "Parameters missing.  Enter values for units (optional, default " \
    #           "is inches), stitches, rows, circum, length, ease (optional, default is -8)."
    #else:
    result = render_template('form.html',
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
