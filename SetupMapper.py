#!/usr/bin/env python2.7
import sys

adj_list = []
actual_node = None

pagerank = 1.0

for line in sys.stdin:

	# Skip the comment and empty lines
	if line.strip() == "" or line[0] == '#':
		continue

	node1, node2 = line.split('\t')
	node1 = node1.strip()
	node2 = node2.strip()


	if actual_node == node1:
		adj_list.append(node2)

	#Otherwise go to different node
	else:
		if actual_node != None:
			print('%s\t%s %s' % (actual_node, str(pagerank), ' '.join(adj_list)))

		actual_node = node1
		adj_list = [node2]

if actual_node != None:
	print('%s\t%s %s' % (actual_node, str(pagerank), ' '.join(adj_list)))
