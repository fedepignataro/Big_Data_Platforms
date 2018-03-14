#!/usr/bin/env python2.7
import sys, os

actual_word = None
actual_count = 0
word = None

for line in sys.stdin:

	word, count = line.split('\t', 1)

	count = int(count)

	# increase count if processing same word
	if actual_word == word:
		actual_count += count
	# Should we find a new word, add the current word and delete the last count
	else:
		if actual_word:
			print('%s\t%s' % (actual_word, actual_count))
		actual_count = count
		actual_word = word

if actual_word == word:
	print('%s\t%s' % (actual_word, actual_count))
