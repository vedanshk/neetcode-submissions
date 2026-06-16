class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        res = {}
        

        for num in nums:
            res[num] = res.get(num, 0) + 1

        ans = sorted(res, key=res.get, reverse=True)[:k]      
        return ans
