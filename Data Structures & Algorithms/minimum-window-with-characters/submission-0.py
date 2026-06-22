class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        myMap= {}
        n = len(s)
        for i in range(len(t)):
            myMap[t[i]] =  myMap.get(t[i] , 0) + 1
        
        result = ""
        resultLen = float("inf")

        need = len(myMap)
        have = 0
        sMap = {}
        for r in range(n):
            sMap[s[r]] =  sMap.get(s[r] , 0) + 1
            if s[r] in myMap:
                if myMap[s[r]] == sMap[s[r]]:
                    have+=1
            while have == need:
                if (r - l + 1) < resultLen:
                    resultLen = r-l +1
                    result = s[l:r+1]
                
                sMap[s[l]] -= 1
                if s[l] in myMap and sMap[s[l]] < myMap[s[l]]:
                    have -= 1
                l+=1
        
        return result
                





            

            


        


        