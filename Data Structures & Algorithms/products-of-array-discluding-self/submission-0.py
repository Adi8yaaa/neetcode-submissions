class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        presum = 1
        for i in range(1,len(nums)):
            presum *= nums[i-1]
            pre[i] = presum
        
        sufsum = 1
        for i in range(len(nums)-2, -1, -1):
            sufsum *= nums[i+1]
            suf[i] = sufsum
        
        for i in range(len(nums)):
            pre[i] = pre[i]*suf[i]
        
        return pre

        

        