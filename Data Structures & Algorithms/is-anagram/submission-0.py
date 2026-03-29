class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort = False
        if sorted(s) == sorted(t):
            sort = True
        return sort
        