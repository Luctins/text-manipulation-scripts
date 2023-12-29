#!/usr/bin/env python3

#conversion modules
from linear import cvt2smc, cvt2sqc, cvt2rdc
from zalgo import cvt2zalgo

#core imports
import os
import argparse

options = {
        'smc': cvt2smc.convert,
        'rdc': cvt2rdc.convert,
        'sqc': cvt2sqc.convert,
        'zalgo': cvt2zalgo.convert,
        'zalgo-1': cvt2zalgo.convert,
        'zalgo-2': lambda x: cvt2zalgo.convert(x, intensity=2),
        'zalgo-3': lambda x: cvt2zalgo.convert(x, intensity=3)
        }

parser = argparse.ArgumentParser(
        prog="Text Converter",
        description="Utility script to convert text to a myriad of 'strange' unicode alternate formats"
        )

parser.add_argument('-i', '--input', type=str)
parser.add_argument('-e', '--espanso', action='store_true', help="Take conversion input directly from espanso environment variable.")
parser.add_argument('-o', '--option', choices=options.keys(), metavar='option', help=f"Conversion type key ({options.keys()})", required=True)

args = parser.parse_args()

if args.espanso:
    inp = os.environ['ESPANSO_INPUT_NAME']
else:
    inp = args.input

print(options[args.option](inp))

