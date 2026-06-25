class Solution:
    def countBits(self, n: int) -> List[int]:

        result  = []

        def count(nums):
            count = 0
            while nums > 0:
                if nums & 1 == 1:
                    count+=1
                
                nums = nums >>1

            return count
        
        for i in range(n+1):
            counts =  count(i)
            result.append(counts)
        

        return result

        