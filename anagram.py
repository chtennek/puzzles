import sys
import json
from collections import defaultdict
import itertools

from buckets import key

def add(letters, bank):
    for l in letters:
        if l not in bank:
            bank[l] = 0
        bank[l] += 1

def subtract(letters, bank):
    for l in letters:
        if l in bank:
            bank[l] -= 1

def contained(letters, bank):
    counts = defaultdict(int)
    add(letters, counts)
    return all(counts[l] <= bank[l] for l in counts)

def anagram(words, bank, min_index):
    if min_index >= len(words) or all(v == 0 for v in bank.values()):
        return []
    anagrams = []
    for i in range(min_index, len(words)):
        if contained(words[i], bank):
            new_bank = bank.copy()
            subtract(words[i], new_bank)

            new_anagrams = anagram(words, new_bank, i)
            if new_anagrams is None:
                continue
            elif len(new_anagrams) == 0:
                anagrams += [words[i]]
            else:
                anagrams += [words[i] + ' ' + w for w in new_anagrams]
    return anagrams if len(anagrams) > 0 else None

def lookup(dictionary, a):
    return itertools.product(*[dictionary[w] for w in a.split()])

if __name__ == '__main__':
    dictionary = json.load(open(sys.argv[1]))
    letters = sys.argv[2]
    bank = defaultdict(int)
    add(letters, bank)

    subwords = defaultdict(list)
    words = []
    for word in dictionary:
        if not contained(word, bank):
            continue

        subwords[len(word)] += [word]
        words += [word]
    words.sort(key=lambda w: (len(w), w), reverse=True)

    anagrams = anagram(words, bank, 0)
    for a in anagrams:
        for b in lookup(dictionary, a):
            print ' '.join(b)
