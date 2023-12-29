#! /usr/bin/env python3

ascii_sequence = 'abcdefghijklmnopqrstuvwxyz'
smc_sequence = 'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ'
rdc_sequence = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
sqc_sequence = '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉'

ascii2rdc = {ascii_sequence[i]: rdc_sequence[i] for i in range(len(rdc_sequence))}
ascii2smc = {ascii_sequence[i]: smc_sequence[i] for i in range(len(smc_sequence))}
ascii2sqc = {ascii_sequence[i]: sqc_sequence[i] for i in range(len(sqc_sequence))}

