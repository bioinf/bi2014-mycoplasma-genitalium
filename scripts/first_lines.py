#!/usr/bin/python3

from itertools import groupby

filepath = input()
result = []
with open(filepath) as f:
	while True:
		line = f.readline()
		if not line:
			break
		if not line.startswith('#'):
			result.append(line)


split_tuples = [string.split() for string in result]
grouped_by_protein = groupby(split_tuples, key=lambda x: x[0])
max_tuples = [max(t[1], key=lambda x: x[2])   for t in grouped_by_protein]
tuples_to_print = [' '.join(l) for l in max_tuples]
print('\n'.join(tuples_to_print))
