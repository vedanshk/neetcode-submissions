class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr , t):
            low =  0 
            high = len(arr)-1
            while low <=high:
                mid = (low + high) // 2

                if arr[mid] == t :
                    return True

                elif arr[mid] < t:
                    low = mid +1
                else:
                    high = mid -1

            return False
        
        for m in matrix:
            if binary_search(m , target):
                return True

        return False
        