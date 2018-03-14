#!/usr/bin/env python2.7
import sys

for line in sys.stdin:

	word, count = line.split('\t', 1)
	word, document = word.split(' ', 1)

	print('%s\t%s' % (document,word + ' ' + count))
