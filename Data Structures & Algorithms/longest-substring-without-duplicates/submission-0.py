class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l , n = 0 , len(s)

        st = set()
        longest = 0

        for r in range(n):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            
            w = (r-l)+1
            longest = max(w , longest)
            st.add(s[r])
        
        return longest


        