class Solution(object):
    def maxScoreSightseeingPair(self, A):
        #O(n)
        result, acc = 0, 0
        for x in A:
            result = max(result, acc+x)
            acc = max(acc, x)-1
        return result
