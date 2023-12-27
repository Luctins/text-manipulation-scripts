#!/bin/env python3

import argparse

import zalgo

commands = {
    'zalgo-1': zalgo.zalgo_convert,
    'zalgo-2': lambda x: zalgo.zalgo_convert(x, intensity=2),
    'zalgo-3': lambda x: zalgo.zalgo_convert(x, intensity=2),
}

parser = argparse.ArgumentParser(
    prog="Text Converter",
    description="Utility script to covert text to a myriad of 'strange'\
    unicode alternate formats",
)
parser.add_argument('mode', choices=commands.keys())
parser.add_argument('input', type=ascii)

args = parser.parse_args()

print(commands[args.mode](args.input))
