class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for a in s:
            if stack and stack[-1] == a:
                stack.pop()
            else:
                stack.append()
        return "".join(stack)
        