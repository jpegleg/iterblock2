import sys
import itertools

characters = (str(sys.argv[1]))
counts = (int(sys.argv[2]))

iblock = itertools.product(characters, repeat=counts)

def iterated(iblock):
    for i in iblock:
        print (''.join(i))

iterated(iblock)        
