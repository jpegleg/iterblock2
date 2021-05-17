import itertools
import json
import sys
import os

try:
    with open("./iterblock.json", "r") as f:
        gconfig = json.load(f)
    diskCheck = str(gconfig["DISKCHECK"])
except Exception:
    diskCheck = str('inactive')

try:
    characters = (str(sys.argv[1]))
except Exception:
    sys.exit('No valid str provided as first argument! Pass a string as the first argument to the script: python3 iterblock.py "abc" 3')

try:
    counts = (int(sys.argv[2]))
except Exception:
    sys.exit('No valid int provided as second argument! Pass an integer as the second argument to the script: python3 iterblock.py "abc" 8')

characters = set(characters)

iblock = itertools.product(characters, repeat=counts)

def diskcheck():
    '''Check disk usage'''
    sized = 'df . | tail -n1 | awk \'{print $5}\' | grep "^9\|^100"'
    alertsize = os.system(sized)
    if alertsize == 0:
        sys.exit("Exiting because disk space usage is 90% or greater in the $pwd partition.")

def iteratedCareful(iblock):
    '''If the DISKCHECK config value is enable, check disk, otherwise just execute the iteration.'''
    for i in iblock:
        diskcheck()
        print (''.join(i))

def iterated(iblock):
    '''If the DISKCHECK config value is enable, check disk, otherwise just execute the iteration.'''
    for i in iblock:
        print (''.join(i))


if diskCheck == "enable":
    iteratedCareful(iblock)
else:
    iterated(iblock)
