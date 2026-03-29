class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snum = sorted(nums)
        dup = False
        for n in range(1,len(nums)):
            if snum[n] == snum[n-1]:
                dup = True
        return dup
        