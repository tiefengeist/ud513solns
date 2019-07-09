import itertools


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):

        if len(words1) != len(words2): return False
        lookup = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in lookup or (w2, w1) in lookup \
                   for w1, w2 in itertools.izip(words1, words2))
