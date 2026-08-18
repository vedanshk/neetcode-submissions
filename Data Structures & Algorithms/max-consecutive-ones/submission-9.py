class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maximum = 0

        streak = 0


        for i in range(0  , len(nums)):

            if nums[i] == 1:
                streak +=1
                maximum = max(maximum , streak)
            else:
                streak = 0

                



        return maximum