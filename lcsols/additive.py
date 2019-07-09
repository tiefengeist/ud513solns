class Solution(object):
    def isAdditiveNumber(self, num):
        def add(a, b):
            res, forward, val = "", 0, 0
            for i in xrange(max(len(a), len(b))):
                val = forward
                if i < len(a):
                    val += int(a[-(i + 1)])
                if i < len(b):
                    val += int(b[-(i + 1)])
                forward, val = val / 10, val % 10
                res += str(val)
            if forward:
                res += str(forward)
            return res[::-1]

            #O(n^2) complexity
        for i in xrange(1, len(num)):
            for j in xrange(i + 1, len(num)):
                s1, s2 = num[0:i], num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or \
                   (len(s2) > 1 and s2[0] == '0'):
                    continue

                expected = add(s1, s2)
                acc = s1 + s2 + expected
                while len(acc) < len(num):
                    s1, s2, expected = s2, expected, add(s2, expected)
                    acc += expected
                if acc == num:
                    return True
        return False
