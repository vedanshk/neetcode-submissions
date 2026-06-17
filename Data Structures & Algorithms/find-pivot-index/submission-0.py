class Solution:
    def pivotIndex(self, arr: List[int]) -> int:

        total =  sum(arr)
        left  = 0

        for i in range(len(arr)):
            total -=arr[i]

            if left == total:
                return i
            
            left+=arr[i]

        
        return -1
            
        