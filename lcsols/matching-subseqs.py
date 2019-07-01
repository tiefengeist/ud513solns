import collections


class Solution(object):
    def numMatchingSubseq(self, S, words):
        towait = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            towait[next(it, None)].append(it)
        for c in S:
            for it in towait.pop(c, ()):
                towait[next(it, None)].append(it)
        return len(towait[None])
