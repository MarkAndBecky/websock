__author__ = 'becky'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import argparse

class Pattern_info(object):

    def __init__(self, units = "inches", stitches=24, rows=30, ease=-8):
        self.units = units
        self.stitches = float(stitches)
        self.rows = float(rows)
        self.ease = float(ease)
        if self.units == "inches":
            self.st_gauge = self.stitches / 4
            self.r_gauge = self.rows / 4
        elif self.units == "cms":
            self.st_gauge = self.stitches / 10
            self.r_gauge = self.rows / 10


def cast_on_stitches(pattern_info, foot_circum):
    """
    Calculates number of stitches to provisionally cast on to start short row toe.
    Ease should be entered as a percentage, negative or positive (usually negative for socks).
    """
    sock_circum = float(foot_circum) + (float(foot_circum) * (pattern_info.ease/100))
    cast_on = round((float(sock_circum) * pattern_info.st_gauge) / 2)
    return cast_on




def short_row_end_stitches(cast_on_sts, percent_end):
    """
    Calcuates number of stitches at end of short row toe or heel; this number is even if the number of toe/heel stitches is even,
    and odd if the number of toe/heel stitches is odd.
    percent_end is the percentage of stitches at the end of toe/heel (usually 40% for toe and 50% for heel)
    """

    x = round(cast_on_sts * (float(percent_end)/100))

    if cast_on_sts % 2 == 0:  # if starting stitches are an even number
        if x % 2 == 0:
            return x
        else:
            if x > cast_on_sts * percent_end:
                return x - 1
            else:
                return x + 1
    else:  # if starting stitches are an odd number
        if x % 2 == 0:
            if x >= cast_on_sts * percent_end:
                return x + 1
            else:
                return x - 1
        else:
            return x


def short_row_end_test():
    print "Test short row end sts:"
    toe_stitch_list = [24, 26, 28, 30, 32, 34, 36, 37]
    for i in toe_stitch_list:
        print "Toe stitches: ", i, "; toe end sts: ", short_row_end_stitches(int(i), 40)
        print "Heel stitches: ", i, "; heel end sts: ", short_row_end_stitches(int(i), 50)


def short_row_length(cast_on_sts, short_row_end_stitches, pattern_info):
    """
    Calculate length of the short row toe or heel.
    """
    short_rows = cast_on_sts - short_row_end_stitches
    sr_length = short_rows / pattern_info.r_gauge
    return sr_length



def pattern(pattern_info, foot_circum, foot_length):

    cast_on = cast_on_stitches(pattern_info, foot_circum)
    heel_end = short_row_end_stitches(cast_on, 50)
    toe_end = short_row_end_stitches(cast_on, 40)
    heel_length = short_row_length(cast_on, heel_end, pattern_info)

    print cast_on, heel_end, toe_end, heel_length
    return cast_on, heel_end, toe_end, heel_length



def main():
    pass


if __name__ == '__main__':
    main()