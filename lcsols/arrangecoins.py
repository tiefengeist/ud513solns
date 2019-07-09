class Solution(object):
    def arrangeCoins(self, n):
#O(log n) due to sqrt function. Trivial solution
        return int((math.sqrt(8*n+1)-1) / 2)
