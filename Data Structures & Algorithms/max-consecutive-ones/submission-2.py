class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max = 0

        for x in nums:
            if x == 1:
                current =  current +1
                if current > max:
                    max = current
            else:
                current = 0

        return max



        