#!/usr/bin/env python2.7
import sys

for line in sys.stdin:

	line = line.strip()

	node, value = line.split('\t', 1)
	pagerank, adjlist = value.split(' ', 1)
	pagerank = float(pagerank)
	adjlist = adjlist.split(' ')

	# Score for each node
	for out_node in adjlist:
		print('%s\tscore %s' % (out_node, str(pagerank/float(len(adjlist)))))

	# Also print the adjacency list
	print('%s\tnode %s' % (node, ' '.join(adjlist)))
