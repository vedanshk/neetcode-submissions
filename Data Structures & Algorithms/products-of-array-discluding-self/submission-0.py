class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n =  len(nums)
        ans = [1] *n

        for i in range(len(nums)):
            ans[i] =  prefix
            prefix*=nums[i]

        suffix =1

        for i in range(n-1 , -1 , -1):
            ans[i] *= suffix
            suffix*= nums[i]



        return ans
        

        