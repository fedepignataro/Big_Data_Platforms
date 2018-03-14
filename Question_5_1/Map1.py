#!/usr/bin/env python2.7
import sys, os


stopwords = {'a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
            'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
            'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
            'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
            'when','where','which','while','who','whom','why','will','with','would','yet','you','your'}

for line in sys.stdin:

	# Get the name of the file we're currently processing
	filename = os.path.basename(os.environ["mapreduce_map_input_file"])

	words = line.split(' ')
	for word in words:
		word = filter(str.isalpha, word).lower()

		if word == "" or word in stopwords:
			continue

		key = word + ' ' + filename;
		print('%s\t%s' % (key, 1))
