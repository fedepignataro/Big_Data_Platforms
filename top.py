import sys

#list of top20 words
top_words = []

for line in sys.stdin:

	key, tf_idf = line.split('\t', 1)
	word, doc = key.split(' ', 1)

	top_words.append((word, tf_idf.strip()))

output = sorted(top_words, key=lambda x: x[1], reverse=False)[:20]

for w, v in output:
	print(w, v)
