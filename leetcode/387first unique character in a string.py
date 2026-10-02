class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        for a in s:
            count[a] = count.get(a,0)+1

        for i,a in enumerate(s):
            if count[a] == 1:
                return i
        return -1