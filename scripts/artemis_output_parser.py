#1/usr/bin/env python
from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        print('No path to Artemis output')
        exit()
    PATH = argv[1]
    missing = 0
    additional = 0
    with open(PATH) as infile:
        for left, right in (line.split() for line in filter(lambda line: not line.startswith('#'), (line.strip() for line in infile.readlines()))):
            if not 'm' in right:
                continue
            print(left, right)
            if left.startswith('+'):
                additional += 1
            else:
                missing += 1
    print('Additional genes: {0}'.format(additional))
    print('Missing genes: {0}'.format(missing))
