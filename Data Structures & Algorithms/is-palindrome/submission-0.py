class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        res = True
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-= 1
            elif s[l].isalnum() and s[r].isalnum() and s[l].lower() == s[r].lower():
                l+= 1
                r-= 1
            else:
                res = False
                break
        return res

        