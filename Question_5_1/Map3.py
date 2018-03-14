#!/usr/bin/env python2.7
import sys

for line in sys.stdin:

	key, val = line.split('\t', 1)
	word, doc = key.split(' ', 1)
	
	count_word, words_per_doc = val.split(' ', 1)

	print('%s\t%s %s %s' % (word, doc, count_word, words_per_doc))
