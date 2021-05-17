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
    '''Check disk usage via system shell, using the linux or bsd df, tail, awk, and grep.'''
    sized = 'nice df . | tail -n1 | awk \'{print $5}\' | grep "^9\|^100"'
    # Best practice would be to move this to subshell instead of using os.system,
    # however I don't feel the need to do that in this case. It is a low priority call.
    alertsize = os.system(sized)
    # Check the exit code for "success" being the condition to trigger an exit.
    # The "success" is the exit code 0, which will be returned if the shell program
    # is successful. This will mean that if the shell program exits in error or fails
    # the diskcheck function will not trigger a iterblock.py exit by design.
    # This allows extended compatibility to other systems and de-prioritizes the 
    # disk check with the idea that we typically don't want to do that anyways.
    if alertsize == 0:
        sys.exit("Exiting because disk space usage is 90% or greater in the $pwd partition.")

def iteratedCareful(iblock):
    '''Run a shell and check the df . and ensure not 90% or greater usage or exit. Otherwise iterate.'''
    for i in iblock:
        # Even though this could be included in the iterated function instead of
        # being here in its own function, it is a performance optimization to have 
        # two separate functions with a switch.
        diskcheck()
        print (''.join(i))

def iterated(iblock):
    '''Execute the iteration of all possible values of the character set for the int length string.'''
    for i in iblock:
        print (''.join(i))


if diskCheck == "enable":
    iteratedCareful(iblock)
else:
    iterated(iblock)
