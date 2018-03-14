#!/usr/bin/env python2.7
import sys

actual_node = None
values = []

# Damping factor
d_f = 0.85

# List of lines for same node, although different last line
def process_node(list_lines):


	pagerank = 0
	adjlist = []
	node = None
	for l_l in list_lines:

		nod, value = l_l.split('\t', 1)

		typee, value = value.split(' ', 1)

		# Node line
		if typee == 'node':
			adjlist = value
			node = nod
		# Score line
		elif typee == 'score':
			pagerank += float(value)

	pagerank = (1.0 - d_f) + (d_f * pagerank)

	# If node is None means we didn't find an adjlist for this node
	if node == None:
		pass
	else:
		print('%s\t%s %s' % (node, str(pagerank), adjlist))


for line in sys.stdin:

	line = line.strip()
	node = line.split('\t', 1)[0][:-1]

	# Set the current node
	if actual_node == None:
		actual_node = node

	# Process this node if we have all the information for it
	if actual_node != node:

		# Process the node
		process_node(values)

		# Update to the new current node
		actual_node = node
		values = [line]

	# Otherwise, append the line and continue
	else:
		values.append(line)

if actual_node != None:
	process_node(values)
