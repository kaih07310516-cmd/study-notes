class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        backet = {')' : '(',']' : '[','}':'{'}
        for char in s:
            if char in backet:
                if not stack or stack.pop() != backet[char]:
                    return False
            else:
                stack.append(char)    
        return len(stack) == 0