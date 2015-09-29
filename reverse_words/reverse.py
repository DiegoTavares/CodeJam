#!/usr/bin/env python

import sys


#Each line has L letters and W words
#Reverse words
#Sample:
#   Input                       Output
#   3                           Case #1: test a is this
#   this is a test              Case #2: foobar
#   foobar                      Case #3: base your all
#   all your base


def reverse_phrase(line):
    out_line = []
    words = line[:-1].split(' ')
    out_line = words[::-1]

    return out_line

if len(sys.argv) == 2:
    reverse_lines = []
    with open(sys.argv[1], 'r') as f:
        num_tests = int(f.readline())
        for i in range(num_tests):
            print("Case #%d: %s" %(i+1, " ".join(reverse_phrase(f.readline()))))
