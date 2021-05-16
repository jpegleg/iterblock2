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
    print('No arguments provided! Executing with default character list of alpha-numeric english.')
    os.system('sleep 2')
    characters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

try:
    counts = (int(sys.argv[2]))
except Exception:
    print('No arguments provided! Executing with default number of word-length as 4 characters.')
    os.system('sleep 2')
    counts = int('4')
finally:
    characters = set(characters)

iblock = itertools.product(characters, repeat=counts)

def diskcheck():
    '''Check disk usage'''
    sized = 'df . | tail -n1 | awk \'{print $5}\' | grep "^9\|^100"'
    alertsize = os.system(sized)
    if alertsize == 0:
        sys.exit("Exiting because disk space is 90% or greater in the $pwd")

def iterated(iblock):
    '''If the diskcheck config is set, check disk, otherwise just execute the iteration.'''
    for i in iblock:
        if diskCheck == "enable":
            diskcheck()
        print (''.join(i))


iterated(iblock)
