class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snum = set(nums)
        dup = True
        if sorted(snum) == sorted(nums):
            dup = False
        return dup
            
        
        