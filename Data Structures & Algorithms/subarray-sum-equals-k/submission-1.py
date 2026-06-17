class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0
        mp = {0: 1}

        for x in nums:
            prefix_sum += x

            if prefix_sum - k in mp:
                count += mp[prefix_sum - k]

            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

        return count
