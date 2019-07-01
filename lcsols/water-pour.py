class Solution(object):
    def pourWater(self, height, V, K):
        for _ in xrange(V):
            best = K
            for d in (-1, 1):
                i = K
                while 0 <= i+d < len(height) and \
                      height[i+d] <= heights[i]:
                    if height[i+d] < height[i]: best = i+d
                    i += d
                if best != K:
                    break
            height[best] += 1
        return height
