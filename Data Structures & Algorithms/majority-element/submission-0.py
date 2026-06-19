class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n / 2

        my_map = dict()

        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1

        for key in my_map.keys():
            if my_map.get(key) >= majority:
                return key
