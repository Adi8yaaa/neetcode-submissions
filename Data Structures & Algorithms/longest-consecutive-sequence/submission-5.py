class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = sorted(set(nums))
        if not numset:
            return 0

        longest = 1
        current = 1

        for i in range(1, len(numset)):
            if numset[i] == numset[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)