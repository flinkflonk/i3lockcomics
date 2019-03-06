#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import atexit
from time import time, strftime, localtime
from datetime import timedelta


def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime('%Y-%m-%d %H:%M:%S', localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(_text, elapsed=None):
    out = ''
    if 'start' not in _text.lower():
        out += '\n'
    line = '{}'.format('=' * 40)
    out += '{line}\n'.format(line=line)
    out += '{time} - {_text}\n'.format(time=secondsToStr(), _text=_text)
    if elapsed:
        out += 'Elapsed time: {}\n'.format(elapsed)
    out += '{line}'.format(line=line)
    if 'end' not in _text.lower():
        out += '\n'
    print(out)


def endlog():
    end = time()
    elapsed = end - start
    log('End Program', secondsToStr(elapsed))


start = time()
atexit.register(endlog)
log('Start Program')


if __name__ == '__main__':
    pass