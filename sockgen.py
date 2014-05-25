__author__ = 'becky'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

def gauge(units, stitches, rows):
    """
    Calculates row and stich guage per inch or per cm based on rows and stitches per 4 inches or 10 cm.
    """
    inches = ["inches", "inch", "in", "ins", '"']
    cm = ["centimetres", "centimeters", "cm", "cms"]
    if units.lower() in inches:
        st_gauge = float(stitches) / 4
        r_gauge = float(rows) / 4
        unit_used = "inches"
        return r_gauge, st_gauge, unit_used
    elif units.lower() in cm:
        st_gauge = float(stitches) / 10
        r_gauge = float(rows) / 10
        unit_used = "cms"
        return r_gauge, st_gauge, unit_used
    else:
        print "Units '%s' not recognised" % units


def cast_on_stitches(st_gauge, foot_circum, ease):
    """
    Calculates number of stitches to provisionally cast on to start short row toe.
    Ease should be entered as a percentage, negative or positive (usually negative for socks).
    """
    sock_circum = float(foot_circum) + (float(foot_circum) * (float(ease)/100))
    cast_on = round((float(sock_circum) * st_gauge) / 2)
    print "Foot circumference: %.2f\nSock circumference: %.2f\nCast on for toe: %.2f" % \
          (float(foot_circum), sock_circum, cast_on)
    return cast_on


def short_row_end_stitches(start_stitches, percent):
    """
    Calcuates number of stitches at end of short row toe; this number is even if the number of toe stitches is even,
    and odd if the number of toe stitches is odd.
    """

    x = round(float(start_stitches) * percent)

    if float(start_stitches) % 2 == 0:  # if starting stitches are an odd number
        if x % 2 == 0:
            return x
        else:
            if x > (float(start_stitches) * percent):
                return x - 1
            else:
                return x + 1
    else:  # if starting stitches are an odd number
        if x % 2 == 0:
            if x >= (float(start_stitches) * percent):
                return x + 1
            else:
                return x - 1
        else:
            return x


def short_row_end_test():
    print "Test short row end sts:"
    toe_stitch_list = [24, 26, 28, 30, 32, 34, 36, 37]
    for i in toe_stitch_list:
        print "Toe stitches: ", i, "; toe end sts: ", short_row_end_stitches(int(i), 0.4)
        print "Heel stitches: ", i, "; heel end sts: ", short_row_end_stitches(int(i), 0.5)


def short_row_length(start_stitches, end_stitches, rgauge):
    """
    Calculate length of the short row toe or heel.
    """
    short_rows = start_stitches - end_stitches
    sr_length = short_rows / rgauge
    return sr_length


def get_input():
    """
    Obtain the user input values.
    """
    input_units = raw_input("Units (inch/cm):")
    swatch_stitches = float(raw_input("Stitches per 10cm/4in:"))
    swatch_rows = float(raw_input("Rows per 10cm/4in:"))
    foot_circum = float(raw_input("Foot circumference in %s at widest point:" % input_units))
    foot_length = float(raw_input("Foot length in %s:" % input_units))
    ease = float(raw_input("Ease required in % (standard is -8):"))

    return input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease


def pattern(input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease):

    rgauge, stgauge, units = gauge(input_units, swatch_stitches, swatch_rows)
    cast_on = cast_on_stitches(stgauge, foot_circum, ease)
    heel_end = short_row_end_stitches(cast_on, 0.5)
    toe_end = short_row_end_stitches(cast_on, 0.4)
    heel_length = short_row_length(cast_on, toe_end, rgauge)

    pattern = [
        "TOE",
        "Provisional cast on %d stitches." % cast_on,
        "Knit %d stitches until 1 stitch before end, wrap and turn." % (cast_on -1),
        "Purl %d stitches until 1 stitch before end, wrap and turn." % (cast_on -2),
        "Knit %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -3),
        "Purl %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -4),
        "Continue short rows until %d stitches remain unwrapped.  %d stitches wrapped on each side." % \
          (toe_end, (cast_on - toe_end)/2),
        "Knit %d, pick up and knit wrap and next stitch together, wrap and turn" % toe_end,
        "Purl %d, pick up and purl wrap and next stitch together, wrap and turn" % (toe_end + 1),
        "Knit %d, pick up and knit both wraps and next stitch together, wrap and turn" % (toe_end + 2),
        "Purl %d, pick up and purl both wrap and next stitch together, wrap and turn" % (toe_end + 3),
        "Continue until all wraps have been consumed.",
        "FOOT",
        "Pick up provisional stitches and begin knitting in the round.  First half of stitches will be the sole, second half will be the instep.",
        "Knit until sock measures %.2f %s." % (foot_length - heel_length, units),
        "HEEL",
        "Knit %d stitches until 1 stitch before end of sole stitches, wrap and turn." % (cast_on -1),
        "Purl %d stitches until 1 stitch before end of sole stitches, wrap and turn." % (cast_on -2),
        "Knit %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -3),
        "Purl %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -4),
        "Continue short rows until %d stitches remain unwrapped.  %d stitches wrapped on each side." % \
          (heel_end, (cast_on - heel_end)/2),
        "Knit %d, pick up and knit wrap and next stitch together, wrap and turn" % heel_end,
        "Purl %d, pick up and purl wrap and next stitch together, wrap and turn" % (heel_end + 1),
        "Knit %d, pick up and knit both wraps and next stitch together, wrap and turn" % (heel_end + 2),
        "Purl %d, pick up and purl both wrap and next stitch together, wrap and turn" % (heel_end + 3),
        "Continue until all wraps have been consumed.",
        "LEG",
        "Resume knitting in the round.  Knit until leg is %d %s, or desired length before end ribbing." % \
          (foot_length, units),
        "Switch to K1P1 or K2P2 ribbing for 1 - 1.5 inches or desired length.",
        "Cast off and weave in ends."
        ]
    return pattern


def main():

    parser = argparse.ArgumentParser(description="""Generates a sock pattern with short row heel and toe.""")
    parser.add_argument("-u", "--units", default="inch", help="Units for pattern; enter inches or cm.")
    parser.add_argument("-s", "--swatchstitches", type=int, help='Number of stitches in 4" or 10 cm.')
    parser.add_argument("-r", "--swatchrows", type=int, help='Number of rows in 4" or 10 cm.')
    parser.add_argument("-c", "--circumf", type=int, help="Circumference of foot at widest point in chosen units.")
    parser.add_argument("-l", "--length", type=int, help="Length of foot in chosen units.")
    parser.add_argument("-e", "--ease", type=int, default=-8, help="Ease: enter as +ve or -ve percentage. Default is -8%%.")

    args = parser.parse_args()

    if args.swatchstitches and args.swatchrows and args.circumf and args.length:
        pat = pattern(args.units, args.swatchstitches, args.swatchrows, args.circumf, args.length, args.ease)
    else:
        input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease = get_input()
        pat = pattern(input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease)

    for i in pat:
        print i

if __name__ == '__main__':
    main()