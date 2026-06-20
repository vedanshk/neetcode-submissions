class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        #p[i] -p[j] = max , i < j

        l = 0 
        n = len(prices)

        for r in range(n):

            if prices[r] >  prices[l]:
                curr_profit = prices[r] -  prices[l]
                max_profit = max(max_profit , curr_profit)
            else:
                if prices[r] <= prices[l]:
                    l =r


        return max_profit 



            


        