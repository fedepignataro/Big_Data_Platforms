#!/usr/bin/env python2.7
import sys

actual_doc = None
actual_count = 0
count_word = {}
doc = None


lines = []

for line in sys.stdin:

	if line.strip() == "":
		continue

	# Save for the second iteration
	lines.append(line)

	# Extract the information from the current line
	doc, val = line.split('\t', 1)
	word, count = val.split(' ', 1)
	count = int(count)

	# If we're processing the same document, increase the count
	if actual_doc == doc:
		actual_count += count

	# If we encounter a new document, update the current document and writeout the last wordcount
	else:
		if actual_doc:
			count_word[actual_doc] = actual_count
		actual_count = count
		actual_doc = doc

if actual_doc == doc:
	count_word[actual_doc] = actual_count


for line in lines:
	# Extract the information from the current line
	doc, val = line.split('\t', 1)
	word, count = val.split(' ', 1)
	print('%s %s\t%s %s' % (word, doc, count.strip(), str(count_word[doc])))
