class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # [2 , 4 , 3 , 8 , 1]
        for i in range(n):
            for j in range(n):
                if nums[j] > nums[i]:
                    temp =  nums[i]
                    nums[i] =  nums[j]
                    nums[j] = temp
                
        return nums
        