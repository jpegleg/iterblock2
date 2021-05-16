import itertools
import time
import sys
import os

from datetime import datetime

characters = (str(sys.argv[1]))
counts = (int(sys.argv[2]))

iblock = itertools.product(characters, repeat=counts)

def timeslice():
    '''Make a global TIMESTAMP with datetime module.'''
    global TIMESTAMP
    TIMESTAMP = datetime.now()
    return(TIMESTAMP)

def diskcheck():
    '''Check disk usage'''
    timeslice()
    sized = 'df . | tail -n1 | awk \'{print $5}\' | grep "^9\|^100"'
    alertsize = os.system(sized)
    timeslice()
    if alertsize == 0:
        timeslice()
        sys.exit("Exiting because disk space is 90% or greater in the $pwd")
    else:
        timeslice()
    timeslice()

def iterated(iblock):
    for i in iblock:
        diskcheck()
        print (''.join(i))


iterated(iblock)
