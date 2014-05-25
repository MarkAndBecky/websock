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

    length = float(request.args.get('length', 8))

    ease = float(request.args.get('ease', -8))


    #if stitches == None or rows == None or circum == None or length == None:
    #    return "Parameters missing.  Enter values for units (optional, default " \
    #           "is inches), stitches, rows, circum, length, ease (optional, default is -8)."
    #else:
    result = render_template('form.html',
                             units=units, stitches=stitches, rows=rows, circum=circum, length=length, ease=ease,
                             pattern = sockgen.pattern(units, stitches, rows, circum, length, ease),
                             gauge = sockgen.gauge(units, stitches, rows),)

    return result



if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
