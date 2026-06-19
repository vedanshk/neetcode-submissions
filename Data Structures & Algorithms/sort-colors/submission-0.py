class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if nums[j] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
            
        