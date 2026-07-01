class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        res = []

        def dfs(start , current_combination , remaining_target):

            if remaining_target == 0:
                res.append(current_combination[:])
                return
            if remaining_target <0:
                return 

                    
            for i in range(start , len(nums)):
                current_combination.append(nums[i])

                dfs(i , current_combination , remaining_target-nums[i])

                current_combination.pop()



        dfs(0 , [] , target)       

        return res
        