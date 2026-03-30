class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = True
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (s[i] == ')' and top != '(') or \
                   (s[i] == '}' and top != '{') or \
                   (s[i] == ']' and top != '['):
                    res = False
        return res and len(stack) == 0