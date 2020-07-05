#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1111 1111 1011 1110 1000 1100 1001 0111‬
def yuanma_to_decimal(s):
    return yuanma_to_decimal_basic(s.replace('\u202c', ''))


def yuanma_to_decimal_basic(s):
    if len(s) == 1:
        if s == '1':
            return 1
        else:
            return 0

    if s[-1] == " ":
        return int(yuanma_to_decimal_basic(s[:-1]))

    temp = 2 * yuanma_to_decimal_basic(s[:-1])
    return temp + int(s[-1])


def decimal_to_buma(n):
    if n == 1:
        return '1'

    if n == 0:
        return '0'

    if n % 2 == 0:
        return decimal_to_buma(n // 2) + "0"
    else:
        return decimal_to_buma((n - 1) // 2) + "1"


def qufan(s):
    result = ''
    for c in s:
        if c == '1':
            result += "0"
        else:
            result += '1'
    return result


print(yuanma_to_decimal(qufan(decimal_to_buma(4289384))))
