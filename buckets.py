import sys
import json
from collections import defaultdict

def key(word):
    return ''.join(sorted(word.lower()))

if __name__ == '__main__':
    words = [x.strip() for x in open(sys.argv[1]).readlines()]
    dictionary = defaultdict(list)
    for w in words:
        dictionary[key(w)] += [w]

    with open(sys.argv[2], 'w') as f:
        json.dump(dictionary, f, indent=4)
