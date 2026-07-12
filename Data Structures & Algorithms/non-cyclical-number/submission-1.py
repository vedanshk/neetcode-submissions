class Solution:
    def isHappy(self, n: int) -> bool:
        
        res = 0
        repeat = set()

        while n!=1:
            if n in repeat:
                return False

            total = 0
            repeat.add(n)

            while n > 0:
                remin = n%10
                n = n//10
                total += remin**2

            
            n = total



        return True