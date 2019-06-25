class Solution(object):
    def carPooling(self, trips, capacity):
        q = [x for n, start, end in trips for x in [[start, n], [end, -n]]]
        q.sort()
        for _, n in q:
            cap -= n
            if cap < 0:
                return False
        return True
