class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res =  {}
        for num in nums:
            res[num] =  res.get(num , 0) + 1

        for key, value in res.items():
            if value >= 2:
                return True



        return False

    
        