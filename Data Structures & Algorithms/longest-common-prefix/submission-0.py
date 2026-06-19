class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        first = strs[0]

        for i , c in enumerate(first):
            for s in strs:
                if i >= len(s) or s[i] !=  c:
                    return ans
            
            ans += c
        
        return ans
                    

            
            
            
             



            







        

        