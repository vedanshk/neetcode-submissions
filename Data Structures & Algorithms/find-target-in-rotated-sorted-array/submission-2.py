class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l , r =  0 , len(arr)-1


        while l < r:

            mid = (l+r) //2

            if arr[mid] == target: return mid

            if arr[mid] >  arr[r]:

                if target >= arr[l] and target <= arr[mid]:
                    r = mid -1
                else:
                    l = mid +1

            
            elif arr[r] > arr[mid]:
                if target <= arr[r] and target >= arr[mid]:
                    l = mid +1
                else:
                    r = mid -1 
        
        if arr[l] ==  target:
            return l
        

        return -1
            
            
                
            

        