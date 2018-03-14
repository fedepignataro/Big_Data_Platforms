#!/usr/bin/env python2.7
import sys, math

actual_word = None
count_in_doc = 0
word = None
doc = None
words_per_doc = 0

# An array holding tuples of (count_word, words_in_doc_count) = Bag of Words
BoW = []

for line in sys.stdin:

	if line.strip() == "":
		continue

	word, val = line.split('\t', 1)
	doc, count_wordss, words_per_doc = val.split(' ', 2)

	# count_wordss = count word
	count_wordss = int(count_wordss)
	words_per_doc = int(words_per_doc)

	# If processing the same word, add it to the count
	if actual_word == word:
		BoW.append((count_wordss, words_per_doc, doc))
		count_in_doc += 1
	# Should we find a new word, add the current word and delete the last count
	else:

		# Check if there was a current word
		if actual_word:
			# a = count_wordss
			# b = words_per_doc
			# c = doc
			for a, b, c in BoW:
				tf_idf = (float(a) / float(b)) * math.log(2.0 / float(count_in_doc))
				print '%s %s\t%s' % (actual_word, c, str(tf_idf))

		# Reset the counters
		BoW = [(count_wordss, words_per_doc, doc)]
		actual_word = word
		count_in_doc = 1

if actual_word == word:
	# a = count_wordss
	# b = words_per_doc
	# c = doc
	for a, b, c in BoW:
		tf_idf = (float(a) / float(b)) * math.log(2.0 / float(count_in_doc))
		print '%s %s\t%s' % (actual_word, c, str(tf_idf))
