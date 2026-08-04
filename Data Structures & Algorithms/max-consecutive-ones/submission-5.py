class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maximum = 0
        current = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                    current+=1
                    maximum = max(current  , maximum)
            else:
                current = 0

        return maximum
        