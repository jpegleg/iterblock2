import itertools
import sys
import os

characters = (str(sys.argv[1]))
counts = (int(sys.argv[2]))

iblock = itertools.product(characters, repeat=counts)

def diskcheck():
    '''Check disk usage'''
    sized = 'df . | tail -n1 | awk \'{print $5}\' | grep "^9\|^100"'
    alertsize = os.system(sized)
    if alertsize == 0:
        sys.exit("Exiting because disk space is 90% or greater in the $pwd")

def iterated(iblock):
    for i in iblock:
        diskcheck()
        print (''.join(i))

        
iterated(iblock)
