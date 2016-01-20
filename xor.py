# -*- coding: utf8 -*-
from itertools import izip, cycle

def getXorString(data, key):
	return ''.join(chr(ord(_)^ord(__)) for _, __ in izip(data, cycle(key)))

def main():
	data = 'Hello world, my name is Lin.'
	key = 'UCCU'
	enc = getXorString(data, key)
	print(enc)
	open('enc', 'w').write(enc)
	dec = getXorString(enc, key)
	print(dec)

if(__name__=='__main__'):
	main()
